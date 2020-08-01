'''
Author's: Belochitsky Oleg , Alfi Tal , Friza Ziv
IDs: 321192577, 204557052, 312196355
'''
import numpy as np
import pandas as pd
from numpy import log2 as log

eps = np.finfo(float).eps
'''
'eps' here is the smallest representable number.
 At times we get log(0) or 0 in the denominator,
 to avoid that we are going to use this.
'''


class Id3:
    '''
    atributes:
    target - the classification column
    targetIndex - the classification column index
    otherColumns - all columns that are not the target
    tree - the DT
    '''

    def __init__(self, df, Class, tolorance):
        self.target = Class
        self.targetIndex = list(df.columns).index(Class)
        self.otherColumns = self.getOtherColumns(df)
        self.tolorance = tolorance
        self.tree = self.buildTree(df)

    def find_entropy(self, df):
        '''
        method return the entropy for the classification column
        in the given df
        '''
        entropy = 0
        values = df[self.target].unique()
        for value in values:
            probability = df[self.target].value_counts()[value] / len(df[self.target])
            entropy += - probability * np.log2(probability)
        return entropy

    def find_entropy_attribute(self, df, attribute):
        '''
        method return the entropy of the 'split' via attribute
        '''
        target_variables = df[self.target].unique()  # This gives all 'Yes' and 'No'
        # This gives different features in that attribute (like 'Hot','Cold' in Temperature)
        variables = df[attribute].unique()
        totalEntropy = 0
        for variable in variables:
            entropy = 0
            for target_variable in target_variables:
                num = len(df[attribute][df[attribute] == variable]
                          [df[self.target] == target_variable])

                den = len(df[attribute][df[attribute] == variable])

                probability = num / (den + eps)
                entropy += - probability * log(probability + eps)

            fraction2 = den / len(df)  # the prob of the atribute var
            totalEntropy += - fraction2 * entropy
        return abs(totalEntropy)

    def find_winner(self, df):
        '''
        method return the column with the best ig for the split
        if there is no more columns to split it return None
        '''
        otherColumns = self.getOtherColumns(df)
        if otherColumns.empty:
            return None
        IG = []
        #ig_dict={}

        enthropy = self.find_entropy(df)
        for key in otherColumns:
            IG.append(enthropy -
                      self.find_entropy_attribute(df, key))
            #ig_dict[key] = enthropy - self.find_entropy_attribute(df, key)

        # print(ig_dict)
        maxIG = np.argmax(IG)
        gainPrecentage = (IG[maxIG] / enthropy) * 100
        return (otherColumns[maxIG], gainPrecentage)

    def getOtherColumns(self, df):
        '''
        Method return all columns without target column in given df
        '''
        otherColumns = list(df.keys())
        otherColumns.remove(self.target)
        otherColumns = pd.Index(otherColumns)
        return otherColumns

    def get_subtable(self, df, node, value):
        '''
        Method return subtable with all rows
        where in column 'node' all are value
        and without the node column
        '''
        # removing unneeded rows
        df = df[df[node] == value].reset_index(drop=True)
        # removing the used column
        columns = list(df.columns)
        columns.remove(node)
        df = df[pd.Index(columns)]
        return df

    def getMostCummon(self, df):
        '''
        Method return most cummon cassification in given df
        '''
        values = df[self.target].unique()
        counts = []
        for value in values:
            counts.append(df[self.target].value_counts()[value])
        return values[counts.index(max(counts))]

    def buildTree(self, df):
        '''
        Method recursivly build DT via id3 algorithm.

        ( comments for each step of the id3 inside)
        return DT
        '''
        # Here we build our decision tree

        # Get attribute with maximum information gain and the infogain precent
        node, gainPrecent = self.find_winner(df)
        ###########################################DELETE
        #print(node)
        ###########################################DELETE
        # if gain under tolorance get the mostCummon
        if (gainPrecent < self.tolorance):
            return self.getMostCummon(df)

        # If there is no more attributes for the split
        if node is None:
            return self.getMostCummon(df)

        # Get distinct value of that attribute e.g Salary is node and Low,Med and High are values
        attValue = np.unique(df[node])

        # Create an empty dictionary to create tree
        # if tree is None:
        tree = {}
        tree[node] = {}

        # We make loop to construct a tree by calling this function recursively.
        # In this we check if the subset is pure and stops if it is pure.

        for value in attValue:

            subtable = self.get_subtable(df, node, value)
            clValue, counts = np.unique(subtable[self.target], return_counts=True)

            if len(counts) == 1:  # Checking purity of subset
                tree[node][value] = clValue[0]
            else:
                # Calling the function recursively
                tree[node][value] = self.buildTree(subtable)

        return tree

    def score(self, data):
        '''
        Method classify all the data acording to the date its trained on.
        and returns how mutch the classification was accurate.
        '''
        total, correct = 0, 0
        TP,TN,FP,FN = 0,0,0,0
        # vector is  : example : ( rowIndex , u_from_col1 , u_from_col2, ...... , classif ,..... )

        for vector in data.itertuples():

            correctClassif = vector[self.targetIndex + 1]
            fixedVector = self.fixVector(vector)  # removing index & class columns

            classif = self.classify(fixedVector)
            total += 1
            if (classif == correctClassif):
                correct += 1

            if (classif == 'yes' and correctClassif == 'yes'):
                TP = TP + 1
            if (classif == 'no' and correctClassif == 'no'):
                TN = TN + 1
            if (classif == 'yes' and correctClassif == 'no'):
                FP = FP + 1
            if (classif == 'no' and correctClassif == 'yes'):
                FN = FN + 1

        return {'score':( correct / total ) *100,
                'TP':TP,
                'TN':TN,
                'FP':FP,
                'FN':FN}


    def fixVector(self, vector):
        '''
        Method get vector and 'Fix' it by
        removeing the index column and the classification column
        '''
        vector = list(vector[1:])  # removing index
        vector.pop(self.targetIndex)
        otherColumns = self.otherColumns
        fixedVector = dict()
        for i, col in enumerate(otherColumns):
            fixedVector[col] = vector[i]

        return fixedVector

    def classify(self, vector):
        '''
        Method classify the the given vector
        by traversing the DF
        '''
        t = self.tree
        if not isinstance(t, dict):
            return t

        cur = tuple(t.keys())[0]

        # print(vector)



        while (isinstance(t[cur][vector[cur]], dict)):

            t = t[cur][vector[cur]]
            cur = tuple(t.keys())[0]
            if vector[cur] not in t[cur].keys():
                return "no"

        return t[cur][vector[cur]]


def our_id3_adapter(**kwargs):
    train = kwargs['train']
    test = kwargs['test']
    t = kwargs['tolorance']
    model = Id3(train,'class', t )
    return model.score(test)
