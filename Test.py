import Preprocessing
import Preprocessing as pr
import knn  as knn
import time
import pandas as pd

def foo (**kwargs):                                                # 
    print(kwargs)                                                  # 
    time.sleep(2)                                                  # 
    return { 'score':100 , 'TP':100 , 'TN':200 ,'FP':10 ,'FN':20 } #

OUR_ID3         = foo
ID3             = foo
OUR_NAIVE_BAYES = foo
NAIVE_BAYES     = foo
K_NN            = knn.run 
K_MEANS         = foo
PREPROCESS      = pr.Preprocessing_adapter

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
        
kwargs = {   'test':pd.read_csv('test.csv'),
             'train':pd.read_csv('train.csv'),
             'structure':load_structure(),
             'number_of_bins':3,
             'k':5,
             'tolorance':5,
             'bin_type':'entropy',
             'missing_values': 'remove_nans',  
    }

def execute_update_kwargs( function , **kwargs):
    return {**kwargs,**function(**kwargs)} # old kwags are updated by the returen dict from  the function

functions = {
    'our_id3'        : lambda **kwargs: OUR_ID3(**execute_update_kwargs(PREPROCESS, **kwargs)),
    'id3'            : lambda **kwargs: ID3(**execute_update_kwargs(PREPROCESS, **kwargs)),
    'naive_bayes'    : lambda **kwargs: OUR_NAIVE_BAYES(**execute_update_kwargs(PREPROCESS, **kwargs)),
    'our_naive_bayes': lambda **kwargs: NAIVE_BAYES(**execute_update_kwargs(PREPROCESS, **kwargs)),
    # knn/ kmeans has its own preprossesing
    'knn'            : lambda **kwargs: K_NN(**kwargs),  
    'k_means'        : lambda **kwargs: K_MEANS(**kwargs)
}

# test run example:
print(
functions['knn'](**kwargs)
)