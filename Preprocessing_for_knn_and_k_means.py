#!/usr/bin/python
# -*- coding: utf-8 -*-
# Module: Preprocessing_for_knn_and_k_means.py
import pandas as pd
import numpy as np


class Preprocessing_for_knn_and_k_means():

    def __init__(self, train, test, structure_file_name, numBins=None):
        # self.train_df = self.init_data_frames(train_file_name)
        # self.test_df = self.init_data_frames(test_file_name)
        self.train_df = train
        self.test_df = test
        self.structure_dict_file = self.structure_txt_file_to_dict(
            structure_file_name)
        self.discretization(self.train_df, self.test_df, numBins)

    def init_data_frames(self, csv_file_name):
        return pd.read_csv(csv_file_name).applymap(lambda s: s.lower() if type(s) == str else s)

    def make_bins(self, data, NumBins, column):
        bins = {}
        binsIntervals = np.append(
            np.array([-float('inf')]), np.linspace(min(data), max(data), NumBins - 1))
        binsIntervals = np.append(binsIntervals, np.array([float('inf')]))

        for i in range(len(binsIntervals) - 1):
            bins['{0}'.format(i + 1)] = (binsIntervals[i], binsIntervals[i + 1])
        return bins

    def structure_txt_file_to_dict(self, Structure_open):

        structure_dict = {}
        for line in Structure_open:
            first, *middle, last = line.replace('@ATTRIBUTE', '').split()
            structure_dict[first] = last if '{' not in last else [
                x for x in last[1:-1].split(',')]
        return structure_dict

    def discretization(self, train_data, test_data, NumBins=None):
        self.__replaceNans(train_data)
        self.__alter_binary_columns(train_data,test_data)
        train_data,test_data = self.__remove_non_numeric(train_data,test_data)

        if NumBins == None:
            NumBins = 10

        for column in (list(train_data)[:-1]):
            if self.structure_dict_file[column] == 'NUMERIC':
                self.__replaceCol(self.create_new_column_acording_bins(
                    NumBins, column, train_data), column, train_data)
        self.train_df= train_data
        self.test_df = test_data

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

    def __replaceCol(self, newCol, column, data):
        data[column] = newCol

    def __remove_non_numeric(self, data_train, data_test):
        for key in self.structure_dict_file:
            if self.structure_dict_file[key] != "NUMERIC" and key != "class":
                data_train = data_train.drop([key], axis=1)
                if data_test:
                    data_test = data_test.drop([key], axis=1)
        return [data_train,data_test]

    def __alter_binary_columns(self, data_train, data_test):
        for col in data_train:
            if (self.structure_dict_file[col] == ['yes', 'no'] or self.structure_dict_file[col] == ['no', 'yes']) \
                    and col != "class":
                data_train.loc[data_train[col] == "yes", col] = 1
                data_train.loc[data_train[col] == "no", col] = 0
                if data_test:
                    data_test.loc[data_test[col] == "yes", col] = 1
                    data_test.loc[data_test[col] == "no", col] = 0

                self.structure_dict_file[col] = "NUMERIC"
