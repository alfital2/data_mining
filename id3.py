import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

def id3_adapret(**kwargs):
    # getting data from kwargs
    train = kwargs['train']
    test = kwargs['test']
    t = kwargs['tolorance']
    # bulding encoder
    merged_data = pd.concat([train,test])
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
    # building classification tree 
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=t)
    clf.fit(encoded_train_without_class, encoded_train_classifications)
    # pridicting with the tree
    predictions = clf.predict(encoded_test_without_class)
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
