import pandas as pd
import numpy as np


class Preprocessing():

    def __init__(self, train, test, structure, remove_nans ,numBins=None):
        self.train_df = train
        self.test_df = test
        self.structure_dict_file = self.list_of_strings_to_dict(structure)
        self.discretization(self.train_df, remove_nans, numBins)
        self.discretization(self.test_df, remove_nans, numBins)

    def init_data_frames(self, csv_file_name):
        return pd.read_csv(csv_file_name).applymap(lambda s: s.lower() if type(s) == str else s)

    def make_bins(self, data, NumBins, column):
        bins = {}
        binsIntervals = np.append(
            np.array([-float('inf')]), np.linspace(min(data), max(data), NumBins - 1))
        binsIntervals = np.append(binsIntervals, np.array([float('inf')]))

        for i in range(len(binsIntervals)-1):
            bins['bin{0}'.format(i+1)] = (binsIntervals[i], binsIntervals[i+1])
        return bins

    def list_of_strings_to_dict(self, Structure):
        structure_dict = {}
        for line in Structure:
            first, *middle, last = line.replace('@ATTRIBUTE', '').split()
            structure_dict[first] = last if '{' not in last else [
                x for x in last[1:-1].split(',')]
        return structure_dict

    def discretization(self, data, remove_nans, NumBins=None):

        self.__replaceNans(data)

        for column in (list(data)[:-1]):
            if self.structure_dict_file[column] == 'NUMERIC':
                self.__replaceCol(self.create_new_column_acording_bins(
                    NumBins, column, data), column, data)

    def create_new_column_acording_bins(self, NumBins, column, data):
        bins = self.make_bins(data[column], NumBins, column)
        column_acording_bins = []

        for elm in data[column]:
            for Bin in bins.keys():
                if elm >= (bins[Bin])[0] and elm <= (bins[Bin])[1]:
                    column_acording_bins.append(Bin)
                    break
        return column_acording_bins

    def __replaceNans(self, data):
        data.fillna(data.mode().iloc[0], inplace=True)

    def __dropNans(self,data):
        data.dropna(inplace=True)

    def __replaceCol(self, newCol, column, data):
        data[column] = newCol

def Preprocessing_adapter(**kwargs):
    train = kwargs['train']
    test = kwargs['test']
    structure = kwargs['structure']
    numBins = kwargs['number_of_bins']
    remove_nans = True if kwargs['missing_values'] == 'remove_nans' else False
    inst = Preprocessing( train, test, structure, remove_nans ,numBins)
    return  {'test':inst.test_df ,'train':inst.train_df}

