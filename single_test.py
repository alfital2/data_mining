import pandas as pd
import numpy as np
from start import get_result

# function to open structure file
def load_structure():
    returnList = []
    filename = 'Structure.txt'
    try:
        tmp = open(filename, "r")
        for line in tmp:
            returnList.append(line)
        tmp.close()
    except FileNotFoundError as e:
        print("Error", "file was not found!!")
    return returnList

# the settings for the single test        
kwargs = {   'test':pd.read_csv('test.csv'),
             'train':pd.read_csv('train.csv'),
             'structure':load_structure(),
             'number_of_bins':19,
             'k':5,
             'tolorance':5,
             'bin_type':'entropy',
             'missing_values': 'remove_nans',  
             '8020': 'yes',
    }

# test run example:
print(
get_result('id3',**kwargs)
)