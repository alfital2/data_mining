'''
Author's: Belochitsky Oleg , Alfi Tal , Friza Ziv
IDs: 321192577, 204557052, 312196355
'''
from sklearn.model_selection import train_test_split
import time
import Preprocessing as pr
import knn  as knn
import our_id3 as our_id3
import id3 as id3
import naive_bayes as naive_bayes
import our_naive_bayes as our_nb
import kmeans as km

#     __                                           _       _           
#    / _|                                         | |     | |          
#   | |_ _ __ ___  _ __ ___    _ __ ___   ___   __| |_   _| | ___  ___ 
#   |  _| '__/ _ \| '_ ` _ \  | '_ ` _ \ / _ \ / _` | | | | |/ _ \/ __|
#   | | | | | (_) | | | | | | | | | | | | (_) | (_| | |_| | |  __/\__ \
#   |_| |_|  \___/|_| |_| |_| |_| |_| |_|\___/ \__,_|\__,_|_|\___||___/
#                                                                      
# (from modules)   geting this adapters from other modlues
OUR_ID3         = our_id3.our_id3_adapter
ID3             = id3.id3_adapret
OUR_NAIVE_BAYES = our_nb.run
NAIVE_BAYES     = naive_bayes.naive_bayes_adapter
K_NN            = knn.run 
K_MEANS         = km.run
PREPROCESS      = pr.Preprocessing_adapter

def split_8020(**kwargs):
    df = kwargs['train']
    train, test = train_test_split(df, test_size=0.2, random_state=42, shuffle=True)
    train.dropna(inplace=True)
    test.dropna(inplace=True)
    return {**kwargs,**{'train':train, 'test': test }}

def split_if_needed (**kwargs):
    if kwargs['8020']=='yes':
        return split_8020(**kwargs)
    else:
        return kwargs

def copy_kwargs(**arg_dict):
    kwargs = {**arg_dict, **{'train': arg_dict['train'].copy(deep=True)
                            , 'structure': [x for x in list(arg_dict['structure'])]}
                }
    if(arg_dict['8020'] == 'no'):
        kwargs = {**kwargs , **{'test':arg_dict['test'].copy(deep=True)}}
    return kwargs

def execute_update_kwargs( function , **kwargs):
    return {**kwargs,**function(**kwargs)} # old kwags are updated by the returen dict from  the function

#     __                  _   _                 
#    / _|                | | (_)                
#   | |_ _   _ _ __   ___| |_ _  ___  _ __  ___ 
#   |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#   | | | |_| | | | | (__| |_| | (_) | | | \__ \
#   |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
# (functions)                                              
# cmposing the functions from the modules and the function from above
# to make sure the input does not change we copy is
# than we split if needed
# then we preprocess if its id3 or nb
# then we send the updated kwargs to the classifyer
functions = {
    'our_id3'        : lambda **kwargs: OUR_ID3(**execute_update_kwargs(PREPROCESS, **split_if_needed(**copy_kwargs(**kwargs)))),
    'id3'            : lambda **kwargs: ID3(**execute_update_kwargs(PREPROCESS,**split_if_needed(**copy_kwargs(**kwargs)))),
    'naive_bayes'    : lambda **kwargs: NAIVE_BAYES(**execute_update_kwargs(PREPROCESS,**split_if_needed(**copy_kwargs(**kwargs)))),
    'our_naive_bayes': lambda **kwargs: OUR_NAIVE_BAYES(**execute_update_kwargs(PREPROCESS,**split_if_needed(**copy_kwargs(**kwargs)) )),
    # knn/ kmeans has its own preprossesing
    'knn'            : lambda **kwargs: K_NN(**split_if_needed(**copy_kwargs(**kwargs))),  
    'k_means'        : lambda **kwargs: K_MEANS(**split_if_needed(**copy_kwargs(**kwargs)))
}

# this function should be called from other functions
def get_result(function_name, **kwargs):
    return functions[function_name](**kwargs)
