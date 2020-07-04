#!/usr/bin/python
# -*- coding: utf-8 -*-
# Module: Preprocessing.py
import pandas as pd
import numpy as np


class Preprocessing():

    def __init__(self, train, test, structure_file_name, numBins=None):
        # self.train_df = self.init_data_frames(train_file_name)
        # self.test_df = self.init_data_frames(test_file_name)
        self.train_df = train
        self.test_df = test
        self.structure_dict_file = self.structure_txt_file_to_dict(
            structure_file_name)
        self.discretization(self.train_df, numBins)
        self.discretization(self.test_df, numBins)

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

    def structure_txt_file_to_dict(self, Structure_open):
        structure_dict = {}
        for line in Structure_open:
            first, *middle, last = line.replace('@ATTRIBUTE', '').split()
            structure_dict[first] = last if '{' not in last else [
                x for x in last[1:-1].split(',')]
        return structure_dict

    def discretization(self, data, NumBins=None):
        self.__replaceNans(data)
        if NumBins == None:
            NumBins = 10

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

    def __replaceCol(self, newCol, column, data):
        data[column] = newCol
