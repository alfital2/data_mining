'''
Author's: Belochitsky Oleg , Alfi Tal , Friza Ziv
IDs: 321192577, 204557052, 312196355
'''
import pandas as pd
import Preprocessing_for_knn_and_k_means as PPknn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

from matplotlib import pyplot as plt
import numpy as np




def run(**kwargs ):  # run(files, mode, bins, k=5):

    preprocessor = PPknn.Preprocessing_for_knn_and_k_means(kwargs['train'], kwargs['test'], kwargs['structure'],
                                                           kwargs['number_of_bins'])
    train_features, train_class = get_separated_data(preprocessor, 'train')
    test_features, test_class = get_separated_data(preprocessor, 'test')
    scaler = scaler_initialization(train_features, test_features)
    train_features = scaler.transform(train_features)
    test_features = scaler.transform(test_features)
    classifier = KNeighborsClassifier(n_neighbors=kwargs['k'])
    classifier.fit(train_features, train_class)
    y_pred = classifier.predict(test_features)
    matrix = confusion_matrix(test_class, y_pred)
    report = (classification_report(test_class, y_pred, output_dict=True))
    conclusions = create_conclusions_dictionary(report, matrix)
    return conclusions


def create_conclusions_dictionary(report, matrix):
    return {'score': report['accuracy']*100,
            'TP': matrix[1][1],
            'TN': matrix[0][0],
            'FP': matrix[0][1],
            'FN': matrix[1][0]
            }


def scaler_initialization(train_features, test_features):
    scaler = StandardScaler()
    scaler.fit(train_features)
    scaler.fit(test_features)

    return scaler


def get_separated_data(preprocessor, file_type):
    return [get_features_column(preprocessor, file_type), get_classification_column(preprocessor, file_type)]


def get_features_column(preprocessor, file_type):
    if file_type == 'train':
        return preprocessor.train_df.iloc[:, :-1].values
    elif file_type == 'test':
        return preprocessor.test_df.iloc[:, :-1].values
    pass


def get_classification_column(preprocessor, file_type):
    if file_type == 'train':
        return preprocessor.train_df.iloc[:, -1].values
    elif file_type == 'test':
        return preprocessor.test_df.iloc[:, -1].values
    pass


def init_files(files):
    return [files['structure'], files['train'], files['test']]


# tmp = open("Structure.txt", "r")
# structure_file = []
# for line in tmp:
#     structure_file.append(line)
# tmp.close()
# train = pd.read_csv("train.csv")
# test = pd.read_csv("test.csv")
# ########################
#
#
# kwargs= {'train' : train, 'test' : test , 'structure':structure_file , 'k' : 5 , 'number_of_bins' : 5}
# print(run(**kwargs))

