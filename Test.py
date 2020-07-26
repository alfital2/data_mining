import Preprocessing
import Preprocessing as pr
import knn  as knn
import time
import pandas as pd
import our_id3 as our_id3
import id3 as id3
import naive_bayes as naive_bayes
import kmeans as km

def foo (**kwargs):                                                # 
    print(kwargs)                                                  # 
    time.sleep(2)                                                  # 
    return { 'score':100 , 'TP':100 , 'TN':200 ,'FP':10 ,'FN':20 } #

OUR_ID3         = our_id3.our_id3_adapter
ID3             = id3.id3_adapret
OUR_NAIVE_BAYES = foo
NAIVE_BAYES     = naive_bayes.naive_bayes_adapter
K_NN            = knn.run 
K_MEANS         = km.run
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
    'naive_bayes'    : lambda **kwargs: NAIVE_BAYES(**execute_update_kwargs(PREPROCESS, **kwargs)),
    'our_naive_bayes': lambda **kwargs: OUR_NAIVE_BAYES(**execute_update_kwargs(PREPROCESS, **kwargs)),
    # knn/ kmeans has its own preprossesing
    'knn'            : lambda **kwargs: K_NN(**kwargs),  
    'k_means'        : lambda **kwargs: K_MEANS(**kwargs)
}

# test run example:
print(
functions['id3'](**kwargs)
)