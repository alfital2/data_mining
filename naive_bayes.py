import numpy as np
import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

def naive_bayes_adapter(**kwargs):
    # getting data from kwargs
    train = kwargs['train']
    test = kwargs['test']
    # megreing data to get all uniques and to build encoder for all
    merged_data = pd.concat([train,test])
    # adding unknown uniques to train dataframe 
    # by adding new row with that unknown unique and rest are most cummon uniques
    columns = merged_data.columns
    uniques_lists = dict()
    for col in columns:
        all_elemets = set(merged_data[col].unique())
        uniques_lists[col] = all_elemets.difference(set(train[col].unique()))

    most_cummon = list()
    for col in columns:
        most_cummon.append(train[col].value_counts().idxmax())
    most_cummon = tuple(most_cummon)


    rows_to_add = []
    for i,col in enumerate(columns):
        for unique in uniques_lists[col]:
            rows_to_add.append(most_cummon[:i] + (unique,) + most_cummon[i+1:] )

    train = train.append(pd.DataFrame(rows_to_add, columns=columns))
    # bulding encoder
    merged_data_without_class = merged_data.drop('class',1)
    encoder = OrdinalEncoder()
    encoder.fit(merged_data_without_class)
    # seperating classification column from datasets
    train_without_class= train.drop('class',1)
    test_without_class = test.drop('class',1)
    train_classifications = train['class']
    test_classifications = test['class']
    # encoding them all
    encoded_train_without_class = encoder.transform(train_without_class)
    encoded_test_without_class = encoder.transform(test_without_class)
    encoded_train_classifications = train_classifications.map({'yes':1,'no':0})
    encoded_test_classifications = test_classifications.map({'yes':1,'no':0})
    # building classifer
    clf = CategoricalNB(alpha=1) # when alpha=1 its Laplace smoothing
    clf.fit(encoded_train_without_class, encoded_train_classifications)
    # pridicting with the tree
    predictions = clf.predict(encoded_test_without_class )
    # buildding matrix and cakculating score
    correct = 0
    TP,TN,FP,FN = 0,0,0,0
    for classif, predic in zip(encoded_test_classifications, predictions):
        if (classif == predic):
            correct += 1
        if (classif == 1 and predic == 1 ):
            TP = TP + 1
        if (classif == 0 and predic == 0 ):
            TN = TN + 1
        if (classif == 0 and predic == 1 ):
            FP = FP + 1
        if (classif == 1  and predic == 0 ):
            FN = FN + 1
    total = len(predictions)
    # returning dict acording to the dapter
    return {'score':( correct / total ) *100,
            'TP':TP,
            'TN':TN,
            'FP':FP,
            'FN':FN}
