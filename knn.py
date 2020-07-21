import pandas as pd
import numpy as np
import Preprocessing_for_knn_and_k_means as PPknn
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt

###################### FILES READER
tmp = open("Structure.txt", "r")
structure_file = []
for line in tmp:
    structure_file.append(line)
tmp.close()
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
########################

preprocessor = PPknn.Preprocessing_for_knn_and_k_means(train, {}, structure_file, 3)

print(preprocessor)


train_features = preprocessor.train_df.iloc[:, :-1].values
train_class = preprocessor.train_df.iloc[:, -1].values

test_features = preprocessor.test_df.iloc[:, :-1].values
test_class = preprocessor.test_df.iloc[:, -1].values


def run(files,mode,k):
    structure_file, train, test = init_files(files)

    preprocessor = PPknn.Preprocessing_for_knn_and_k_means(train, test, structure_file, 3)
    if mode != "SPLIT_20_80":
        pass



def init_files(files):
    return [files['structure'], files['train'], files['test']]


if False:
    X = preprocessor.train_df.iloc[:, :-1].values
    y = preprocessor.train_df.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    from sklearn.neighbors import KNeighborsClassifier

    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import classification_report, confusion_matrix

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    error = []

    for i in range(1, 40):
        print("iteration number " + str(i))
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        error.append(np.mean(pred_i != y_test))

    plt.figure(figsize=(12, 6))
    plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
             markerfacecolor='blue', markersize=10)
    plt.title('Error Rate K Value')
    plt.xlabel('K Value')
    plt.ylabel('Mean Error')
    plt.show()
    print("preprocessing done")

if True:
    scaler = StandardScaler()
    # scaler.fit(X_train)
    scaler.fit(train_features)
    scaler.fit(test_features)

    # X_train = scaler.transform(X_train)
    # X_test = scaler.transform(X_test)

    train_features = scaler.transform(train_features)
    test_features = scaler.transform(test_features)

    from sklearn.neighbors import KNeighborsClassifier

    classifier = KNeighborsClassifier(n_neighbors=1)
    # classifier.fit(X_train, y_train)
    classifier.fit(train_features, train_class)

    # y_pred = classifier.predict(X_test)
    y_pred = classifier.predict(test_features)

    from sklearn.metrics import classification_report, confusion_matrix

    print(confusion_matrix(test_class, y_pred))
    print(classification_report(test_class, y_pred))

    error = []

    for i in range(1, 40):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(train_features, train_class)
        pred_i = knn.predict(test_features)
        error.append(np.mean(pred_i != test_class))
        print(confusion_matrix(test_class, pred_i))
        print(classification_report(test_class, pred_i))

    plt.figure(figsize=(12, 6))
    plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
             markerfacecolor='blue', markersize=10)
    plt.title('Error Rate K Value')
    plt.xlabel('K Value')
    plt.ylabel('Mean Error')
    plt.show()
    print("preprocessing done")
