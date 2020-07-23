import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder




# predictions = pd.DataFrame(data=dt,columns=["label"])
# predictions["ImageId"] = list(range(1,len(test)+1))


def id3_adapret(**kwargs):
    train = kwargs['train']
    test = kwargs['test']
    t = kwargs['tolorance']


    train_classifications = train['class']
    train_without_class = train.drop('class',1)
    train_maped_classifications = train_classifications.map({'yes':1,'no':0})


    encoder = OrdinalEncoder()
    encoder.fit(train_without_class)
    X_encoded = encoder.transform(train_without_class)
    train_df = pd.DataFrame(X_encoded)
    print(train_df.head())

    # clf = DecisionTreeClassifier(criterion="entropy", max_depth=t)
    # clf.fit(train, train_classifications)
    # dt = clf.predict(test)

    # model = Id3(train,'class', t )
    # print(train.head(dt))
