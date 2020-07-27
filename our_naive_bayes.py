import pandas as pd
import Preprocessing as pr
from sklearn.metrics import confusion_matrix

class naiveBayes:

    def __init__(self, dataSet,testSet, targetCol='class'):
        self.probabilities = {}
        self.dataSet = dataSet
        self.testSet = testSet
        self.targetCol = targetCol
        self.omega = self.classifier_probability()
        self.create_probability_dictionary()
        self.prediction_column = []
        self.prediction()
        self.matrix = confusion_matrix(self.testSet[self.targetCol], self.prediction_column)

    def classifier_probability(self):
        tmp = {}
        for classifier in set(self.dataSet[self.targetCol]):
            tmp[classifier] = list(self.dataSet[self.targetCol]).count(classifier)/len(self.dataSet[self.targetCol])
        return tmp

    def create_probability_dictionary(self):
        for column in (list(self.dataSet)[:-1]):#theta(column number * unic in all set * 2)
            self.probabilities[column] = {}
            for unic in set(self.dataSet[column]):
                self.probabilities[column][unic] = {}
                for classifier in set(self.dataSet[self.targetCol]):
                    self.probabilities[column][unic][classifier] = self.probability_calc(unic, classifier,self.dataSet[column])

    def probability_calc(self,unic, classifier,data_column):
        tmp = zip(data_column, self.dataSet[self.targetCol])
        # Laplace fix
        count = 1
        for elm, Class in tmp:
            if elm == unic and Class == classifier:
                count += 1
        return count / list(self.dataSet[self.targetCol]).count(classifier)

    def prediction(self):
        winner = {}
        p = 1
        for vector in self.testSet.iloc[:, :-1].itertuples():
            for classifier in set(self.testSet[self.targetCol]):
                for unic in list(vector[1:]):
                    if(self.return_probability_from_probability_dictionary(unic,classifier)!=None):
                        p *= self.return_probability_from_probability_dictionary(unic, classifier)

                winner[p*self.omega[classifier]] = classifier
                p = 1
            self.prediction_column.append(winner[max(winner.keys())])
            winner = {}
        print(len(self.prediction_column))


    def score(self):
        correct_decisions = 0
        tmp = zip(self.prediction_column,self.testSet[self.targetCol])
        for element,prediction in tmp:
            if element == prediction:
                correct_decisions+=1
        return correct_decisions/len(self.testSet)*100

    def return_probability_from_probability_dictionary(self,unic,classifier):
        for column in self.probabilities.keys():
            for this_unic in self.probabilities[column].keys():
                if this_unic == unic:
                    return self.probabilities[column][unic][classifier]

def run(**kwargs ):
    nb = naiveBayes(kwargs['train'], kwargs['test'])
    return {'score': nb.score(),
            'TP': nb.matrix[1][1],
            'TN': nb.matrix[0][0],
            'FP': nb.matrix[0][1],
            'FN': nb.matrix[1][0]
            }
######################################Preprocessing
# tmp = open("Structure.txt", "r")
# structure_file = []
#
# for line in tmp:
#     structure_file.append(line)
# tmp.close()
# train = pd.read_csv('train.csv')
# test = pd.read_csv('test.csv')
# my_pre = pr.Preprocessing(train,test,structure_file,15,'equal_width','remove_nans')
# # ######################################
# nb = naiveBayes(my_pre.train_df,my_pre.test_df)
# print(nb.score())
# print(nb.matrix)




