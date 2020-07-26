import pandas as pd
import numpy as np
# replace_nans
# remove_nans
class Preprocessing():

    def __init__(self,train, test, structure, number_of_bins, bin_type, deal_with_missing):
        self.bins_dict_range = {}
        self.train_df = train
        self.test_df = test
        self.structure_dict_file = self.list_of_strings_to_dict(structure)
        self.discretization(self.train_df,deal_with_missing , bin_type, number_of_bins)
        self.discretization_test(self.test_df, deal_with_missing, bin_type)

    def init_data_frames(self, csv_file_name):
        return pd.read_csv(csv_file_name).applymap(lambda s: s.lower() if type(s) == str else s)


    def list_of_strings_to_dict(self, Structure):
        structure_dict = {}
        for line in Structure:
            first, *middle, last = line.replace('@ATTRIBUTE', '').split()
            structure_dict[first] = last if '{' not in last else [
                x for x in last[1:-1].split(',')]
        return structure_dict

    def add_inf_values(self, bins_array):
        bins_array[0] = np.array([-float('inf')])
        bins_array[len(bins_array) - 1] = np.array([float('inf')])

    def discretization(self, data, Nones, strategy, number_of_bins=None):
        self.Nones_action(data,Nones)
        if strategy == 'equal_width':
            self.equal_width_or_frequency(data, pd.cut, number_of_bins)

        elif strategy == 'equal_frequency':
            self.equal_width_or_frequency(data, pd.qcut, number_of_bins)

    def Nones_action(self,data,Nones):
        if Nones == "remove_nans":
            self.__dropNans(data)
        elif Nones == "replace_nans":
            self.__replaceNans(data)

    def equal_width_or_frequency(self, data, func, number_of_bins):
        for column in (list(data)[:-1]):
            if self.structure_dict_file[column] == 'NUMERIC':
                binned_column = func(np.array(data[column]), number_of_bins, duplicates='drop', retbins=True)
                bins = [x + 1 for x in range(len(binned_column[1]) - 1)]
                binned_column = func(np.array(data[column]), number_of_bins, labels=bins, duplicates='drop',
                                     retbins=True)
                # getting the array of bins the way pandas made it
                self.bins_dict_range[column] = binned_column[1]
                self.__replaceCol(binned_column[0], column, data)
                self.add_inf_values(self.bins_dict_range[column])

    def discretization_test(self, data, Nones, strategy):
        self.Nones_action(data,Nones)
        if strategy == 'equal_width':
            self.create_new_column_according_bins(data)
        elif strategy == 'equal_frequency':
            self.create_new_column_according_bins(data)

    def create_new_column_according_bins(self, data):
        for column in (list(data)[:-1]):
            binned_column = []
            if self.structure_dict_file[column] == 'NUMERIC':
                bins = self.bins_dict_range[column]
                for elm in data[column]:
                    for Bin in range(len(bins)):
                        if bins[Bin] <= elm <= bins[Bin + 1]:
                            binned_column.append(Bin + 1)
                            break
                data[column] = binned_column

    def __replaceNans(self, data):
        data.fillna(data.mode().iloc[0], inplace=True)

    def __dropNans(self, data):
        data.dropna(inplace=True)

    def __replaceCol(self, newCol, column, data):
        data[column] = newCol


def Preprocessing_adapter(**kwargs):
    train = kwargs['train']
    test = kwargs['test']
    structure = kwargs['structure']
    number_of_bins = kwargs['number_of_bins']
    bin_type = kwargs['bin_type']
    deal_with_missing = kwargs['missing_values']
    inst = Preprocessing(train, test, structure, number_of_bins, bin_type, deal_with_missing)
    return {'test': inst.test_df, 'train': inst.train_df}


# ###########
# tmp = open("Structure.txt", "r")
# structure_file = []
# for line in tmp:
#     structure_file.append(line)
# tmp.close()
# train = pd.read_csv("train.csv")
# test = pd.read_csv("test.csv")
# ########################
#
# kwargs={'train' : train, 'test':test, 'structure' :structure_file,  'number_of_bins': 3,
#         'missing_values' : 'replace', 'strategy':'equal_frequency' }
# #Preprocess = Preprocessing(train, test, structure_file, True, 'equal_frequency', 3)
# # Preprocess = Preprocessing(train, test, structure_file, "replace", 'equal_width', 3)
#
# Preprocess = Preprocessing(**kwargs)
# print(Preprocess.train_df['duration'][19])