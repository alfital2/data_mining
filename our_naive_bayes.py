'''
Author's: Belochitsky Oleg , Alfi Tal , Friza Ziv
IDs: 321192577, 204557052, 312196355
'''
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
        return (list(tmp).count((unic, classifier))+1)/\
               list(self.dataSet[self.targetCol]).count(classifier) #+1 for laplace fix

    def prediction(self):
        winner = {}
        p = 1
        for vector in self.testSet.iloc[:, :-1].itertuples():
            for classifier in set(self.testSet[self.targetCol]):
                for unic in list(vector[1:]):
                    c_p = self.return_probability_from_probability_dictionary(unic,classifier,list(vector[1:]).index(unic))
                    if(c_p!=None):
                        p *= c_p
                winner[p*self.omega[classifier]] = classifier
                p = 1
            self.prediction_column.append(winner[max(winner.keys())])
            winner = {}

    def return_probability_from_probability_dictionary(self,unic,classifier,column_index):
        column = list(self.testSet)[column_index]
        try:
            return self.probabilities[column][unic][classifier]
        except KeyError as e:
            return 1

    def score(self):
        correct_decisions = 0
        tmp = zip(self.prediction_column,self.testSet[self.targetCol])
        for element,prediction in tmp:
            if element == prediction:
                correct_decisions+=1
        return correct_decisions/len(self.testSet)*100



def run(**kwargs ):
    nb = naiveBayes(kwargs['train'], kwargs['test'])
    return {'score': nb.score(),
            'TP': nb.matrix[1][1],
            'TN': nb.matrix[0][0],
            'FP': nb.matrix[0][1],
            'FN': nb.matrix[1][0]
            }







