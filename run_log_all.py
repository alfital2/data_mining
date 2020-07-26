
import Preprocessing
import Preprocessing as pr
from sklearn.model_selection import train_test_split
import knn  as knn
import time
import pandas as pd
import numpy as np
import our_id3 as our_id3
import id3 as id3
import naive_bayes as naive_bayes
import kmeans as km
'''
                 bbbbbbbb                                                                    
                 b::::::b                                                      tttt          
                 b::::::b                                                   ttt:::t          
                 b::::::b                                                   t:::::t          
                  b:::::b                                                   t:::::t          
  aaaaaaaaaaaaa   b:::::bbbbbbbbb       ooooooooooo   uuuuuu    uuuuuuttttttt:::::ttttttt    
  a::::::::::::a  b::::::::::::::bb   oo:::::::::::oo u::::u    u::::ut:::::::::::::::::t    
  aaaaaaaaa:::::a b::::::::::::::::b o:::::::::::::::ou::::u    u::::ut:::::::::::::::::t    
           a::::a b:::::bbbbb:::::::bo:::::ooooo:::::ou::::u    u::::utttttt:::::::tttttt    
    aaaaaaa:::::a b:::::b    b::::::bo::::o     o::::ou::::u    u::::u      t:::::t          
  aa::::::::::::a b:::::b     b:::::bo::::o     o::::ou::::u    u::::u      t:::::t          
 a::::aaaa::::::a b:::::b     b:::::bo::::o     o::::ou::::u    u::::u      t:::::t          
a::::a    a:::::a b:::::b     b:::::bo::::o     o::::ou:::::uuuu:::::u      t:::::t    tttttt
a::::a    a:::::a b:::::bbbbbb::::::bo:::::ooooo:::::ou:::::::::::::::uu    t::::::tttt:::::t
a:::::aaaa::::::a b::::::::::::::::b o:::::::::::::::o u:::::::::::::::u    tt::::::::::::::t
 a::::::::::aa:::ab:::::::::::::::b   oo:::::::::::oo   uu::::::::uu:::u      tt:::::::::::tt
  aaaaaaaaaa  aaaabbbbbbbbbbbbbbbb      ooooooooooo       uuuuuuuu  uuuu        ttttttttttt 

this is the run all and log module
----------------------------------
this module is here to run and log expirements without the gui
mainly to queue alot of tests run, run them , creat csv to plot 
at the Jupiter note book

content:
*******
utility:
    In section we have function that help us to connect all
    like file opening functions, csv creating function, the imported classifayer function
    are also setted up here and composed at the right order.
    
tests:
    In this section we have:
    - the default agruments for all the test
    - the tests that will be runned at the driver section

driver: 
    - running the tests
    - creating the csv's
'''
'''
                         tttt            iiii  lllllll   iiii          tttt                               
                      ttt:::t           i::::i l:::::l  i::::i      ttt:::t                               
                      t:::::t            iiii  l:::::l   iiii       t:::::t                               
                      t:::::t                  l:::::l              t:::::t                               
uuuuuu    uuuuuuttttttt:::::ttttttt    iiiiiii  l::::l iiiiiiittttttt:::::tttttttyyyyyyy           yyyyyyy
u::::u    u::::ut:::::::::::::::::t    i:::::i  l::::l i:::::it:::::::::::::::::t y:::::y         y:::::y 
u::::u    u::::ut:::::::::::::::::t     i::::i  l::::l  i::::it:::::::::::::::::t  y:::::y       y:::::y  
u::::u    u::::utttttt:::::::tttttt     i::::i  l::::l  i::::itttttt:::::::tttttt   y:::::y     y:::::y   
u::::u    u::::u      t:::::t           i::::i  l::::l  i::::i      t:::::t          y:::::y   y:::::y    
u::::u    u::::u      t:::::t           i::::i  l::::l  i::::i      t:::::t           y:::::y y:::::y     
u::::u    u::::u      t:::::t           i::::i  l::::l  i::::i      t:::::t            y:::::y:::::y      
u:::::uuuu:::::u      t:::::t    tttttt i::::i  l::::l  i::::i      t:::::t    tttttt   y:::::::::y       
u:::::::::::::::uu    t::::::tttt:::::ti::::::il::::::li::::::i     t::::::tttt:::::t    y:::::::y        
 u:::::::::::::::u    tt::::::::::::::ti::::::il::::::li::::::i     tt::::::::::::::t     y:::::y         
  uu::::::::uu:::u      tt:::::::::::tti::::::il::::::li::::::i       tt:::::::::::tt    y:::::y          
    uuuuuuuu  uuuu        ttttttttttt  iiiiiiiilllllllliiiiiiii         ttttttttttt     y:::::y           
                                                                                       y:::::y            
                                                                                      y:::::y             
                                                                                     y:::::y              
                                                                                    y:::::y               
                                                                                   yyyyyyy   
'''
OUR_ID3         = our_id3.our_id3_adapter
ID3             = id3.id3_adapret
OUR_NAIVE_BAYES = lambda **kwargs : { 'score':100 , 'TP':100 , 'TN':200 ,'FP':10 ,'FN':20 }
NAIVE_BAYES     = naive_bayes.naive_bayes_adapter
K_NN            = knn.run 
K_MEANS         = km.run
PREPROCESS      = pr.Preprocessing_adapter
############################### for testing ##########################################################
OUR_ID3         =lambda **kwargs : { 'score':111 , 'TP':111 , 'TN':111 ,'FP':111,'FN':111}
ID3             =lambda **kwargs : { 'score':222 , 'TP':222 , 'TN':222 ,'FP':222 ,'FN':222 }
OUR_NAIVE_BAYES =lambda **kwargs : { 'score':333 , 'TP':333 , 'TN':333 ,'FP':333 ,'FN':333 }
NAIVE_BAYES     =lambda **kwargs : { 'score':444 , 'TP':444 , 'TN':444 ,'FP':444 ,'FN':444 }
K_NN            =lambda **kwargs : { 'score':555 , 'TP':555 , 'TN':555 ,'FP':555 ,'FN':555 }
K_MEANS         =lambda **kwargs : { 'score':666 , 'TP':666 , 'TN':666 ,'FP':666 ,'FN':666 }
PREPROCESS      =lambda **kwargs : { 'score':777 , 'TP':777 , 'TN':777 ,'FP':777 ,'FN':777 }
####################################################################################################

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
        
def copy_kwargs(**arg_dict):
    kwargs = {**arg_dict, **{'train': arg_dict['train'].copy(deep=True)
                            , 'structure': [x for x in list(arg_dict['structure'])]}
                }
    if(arg_dict['8020'] == pass_kwargs):
        kwargs = {**kwargs , **{'test':arg_dict['test'].copy(deep=True)}}
    return kwargs

def execute_update_kwargs( function , **kwargs):
    return {**kwargs,**function(**kwargs)} # old kwags are updated by the returen dict from  the function

functions = {
    'our_id3'        : lambda **kwargs: OUR_ID3(**execute_update_kwargs(PREPROCESS, **kwargs['8020'](**copy_kwargs(**kwargs)))),
    'id3'            : lambda **kwargs: ID3(**execute_update_kwargs(PREPROCESS,**kwargs['8020'](**copy_kwargs(**kwargs)))),
    'naive_bayes'    : lambda **kwargs: NAIVE_BAYES(**execute_update_kwargs(PREPROCESS,**kwargs['8020'](**copy_kwargs(**kwargs)))),
    'our_naive_bayes': lambda **kwargs: OUR_NAIVE_BAYES(**execute_update_kwargs(PREPROCESS,**kwargs['8020'](**copy_kwargs(**kwargs)) )),
    # knn/ kmeans has its own preprossesing
    'knn'            : lambda **kwargs: K_NN(**kwargs['8020'](**copy_kwargs(**kwargs))),  
    'k_means'        : lambda **kwargs: K_MEANS(**kwargs['8020'](**copy_kwargs(**kwargs)))
}

def pass_kwargs(**kwargs):
    return kwargs

def split_8020(**kwargs):
    df = kwargs['train']
    # train = df.sample(frac=0.8,random_state=200) #random state is a seed value
    # test = df.drop(train.index)
    train, test = train_test_split(df, test_size=0.2, random_state=42, shuffle=True)
    
    train.dropna(inplace=True)
    test.dropna(inplace=True)
    return {**kwargs,**{'train':train, 'test': test }}
                
def df_to_csv (df, filename):
    df.to_csv(filename, encoding='utf-8', index=False)

def matrix_to_df ( columns , matrix):
    d = { k:v for k,v in zip(columns,zip (*matrix))}
    df = pd.DataFrame(d)
    return df

'''
         tttt                                                        tttt                           
      ttt:::t                                                     ttt:::t                           
      t:::::t                                                     t:::::t                           
      t:::::t                                                     t:::::t                           
ttttttt:::::ttttttt        eeeeeeeeeeee        ssssssssss   ttttttt:::::ttttttt        ssssssssss   
t:::::::::::::::::t      ee::::::::::::ee    ss::::::::::s  t:::::::::::::::::t      ss::::::::::s  
t:::::::::::::::::t     e::::::eeeee:::::eess:::::::::::::s t:::::::::::::::::t    ss:::::::::::::s 
tttttt:::::::tttttt    e::::::e     e:::::es::::::ssss:::::stttttt:::::::tttttt    s::::::ssss:::::s
      t:::::t          e:::::::eeeee::::::e s:::::s  ssssss       t:::::t           s:::::s  ssssss 
      t:::::t          e:::::::::::::::::e    s::::::s            t:::::t             s::::::s      
      t:::::t          e::::::eeeeeeeeeee        s::::::s         t:::::t                s::::::s   
      t:::::t    tttttte:::::::e           ssssss   s:::::s       t:::::t    ttttttssssss   s:::::s 
      t::::::tttt:::::te::::::::e          s:::::ssss::::::s      t::::::tttt:::::ts:::::ssss::::::s
      tt::::::::::::::t e::::::::eeeeeeee  s::::::::::::::s       tt::::::::::::::ts::::::::::::::s 
        tt:::::::::::tt  ee:::::::::::::e   s:::::::::::ss          tt:::::::::::tt s:::::::::::ss  
          ttttttttttt      eeeeeeeeeeeeee    sssssssssss              ttttttttttt    sssssssssss 
'''
# default setup:
DEFAULT_TRAIN = pd.read_csv('train.csv')
DEFAULT_TEST = pd.read_csv('test.csv')
DEFAULT_STRUCTURE = load_structure()
DEFAULT_NUMBER_OF_BINS = 10
DEFAULT_BIN_TYPE = 'equal_width'
DEFAULT_TOLORANCE = 5
DEFAULT_K= 5
DEFAULT_8020 = split_8020
DEFAULT_MISSING_VALUES = 'remove_nans'

# for id3 and our_id3
def create_t_test(function_name, tolorance_array):
    arg_dict = {'test': DEFAULT_TEST,
                'train': DEFAULT_TRAIN,
                'structure': DEFAULT_STRUCTURE,
                'tolorance':DEFAULT_TOLORANCE,
                'k':DEFAULT_K,
                'number_of_bins': DEFAULT_NUMBER_OF_BINS,
                'bin_type': DEFAULT_BIN_TYPE,
                'missing_values': DEFAULT_MISSING_VALUES,
                '8020': DEFAULT_8020
                }
    resuluts = []
    for t in tolorance_array:
        result = functions[function_name](**{**arg_dict, **{'tolorance': t}})
        result_tupple = (result['score'], result['TP'],
                         result['TN'], result['FP'], result['FN'], t)
        resuluts.append(result_tupple)
    columns = ('score','TP','TN','FP','FN','t')
    return matrix_to_df(columns, resuluts)

# for knn and kmeans
def create_k_test(function_name, k_array):
    arg_dict = {'test': DEFAULT_TEST,
                'train': DEFAULT_TRAIN,
                'structure': DEFAULT_STRUCTURE,
                'tolorance':DEFAULT_TOLORANCE,
                'k':DEFAULT_K,
                'number_of_bins': DEFAULT_NUMBER_OF_BINS,
                'bin_type': DEFAULT_BIN_TYPE,
                'missing_values': DEFAULT_MISSING_VALUES,
                '8020': DEFAULT_8020
                }
    resuluts = []
    for k in k_array:
        result = functions[function_name]( **{**arg_dict,**{'k':k}} )
        result_tupple = (result['score'],result['TP'],result['TN'],result['FP'],result['FN'],k)
        resuluts.append(result_tupple) 
    columns = ( 'score','TP','TN','FP','FN','k')
    return matrix_to_df(columns, resuluts)

# test for nb, our_nb , id3, our_id3
def create_bins_number_test(function_name, bins_array):
    arg_dict = {'test': DEFAULT_TEST,
                'train': DEFAULT_TRAIN,
                'structure': DEFAULT_STRUCTURE,
                'tolorance':DEFAULT_TOLORANCE,
                'k':DEFAULT_K,
                'number_of_bins': DEFAULT_NUMBER_OF_BINS,
                'bin_type': DEFAULT_BIN_TYPE,
                'missing_values': DEFAULT_MISSING_VALUES,
                '8020': DEFAULT_8020
                }
    resuluts = []
    for b in bins_array:
        result = functions[function_name]( **{**arg_dict,**{'number_of_bins':b}} )
        result_tupple = (function_name, result['score'],result['TP'],result['TN'],result['FP'],result['FN'],b)
        resuluts.append(result_tupple) 
    columns = ( 'function', 'score','TP','TN','FP','FN','number of bins')
    return matrix_to_df(columns, resuluts)

# test for all
def create_nans_test ( function_name ):
    arg_dict = {'test': DEFAULT_TEST,
                'train': DEFAULT_TRAIN,
                'structure': DEFAULT_STRUCTURE,
                'tolorance':DEFAULT_TOLORANCE,
                'k':DEFAULT_K,
                'number_of_bins': DEFAULT_NUMBER_OF_BINS,
                'bin_type': DEFAULT_BIN_TYPE,
                'missing_values': DEFAULT_MISSING_VALUES,
                '8020': DEFAULT_8020
                }
    resuluts = []
    for s in ('remove_nans','replace_nans'):
        result = functions[function_name]( **{**arg_dict,**{'missing_values':s}} )
        result_tupple = (function_name, result['score'],result['TP'],result['TN'],result['FP'],result['FN'],s)
        resuluts.append(result_tupple) 
    columns = ( 'function', 'score','TP','TN','FP','FN','dealing with nans strategy')
    return matrix_to_df(columns, resuluts)

# binning strategy test
def create_bining_strategy_test( function_name ):
    arg_dict = {'test': DEFAULT_TEST,
                'train': DEFAULT_TRAIN,
                'structure': DEFAULT_STRUCTURE,
                'tolorance':DEFAULT_TOLORANCE,
                'k':DEFAULT_K,
                'number_of_bins': DEFAULT_NUMBER_OF_BINS,
                'bin_type': DEFAULT_BIN_TYPE,
                'missing_values': DEFAULT_MISSING_VALUES,
                '8020': DEFAULT_8020
                }
    resuluts = []
    for s in ('equal_width ','equal_frequency', 'entropy'):
        result = functions[function_name]( **{**arg_dict,**{'missing_values':s}} )
        result_tupple = (function_name, result['score'],result['TP'],result['TN'],result['FP'],result['FN'],s)
        resuluts.append(result_tupple) 
    columns = ('function','score','TP','TN','FP','FN','biining strategy')
    return matrix_to_df(columns, resuluts)

def create_split_test ( function_name ):
    arg_dict = {'test': DEFAULT_TEST,
                'train': DEFAULT_TRAIN,
                'structure': DEFAULT_STRUCTURE,
                'tolorance':DEFAULT_TOLORANCE,
                'k':DEFAULT_K,
                'number_of_bins': DEFAULT_NUMBER_OF_BINS,
                'bin_type': DEFAULT_BIN_TYPE,
                'missing_values': DEFAULT_MISSING_VALUES,
                '8020': DEFAULT_8020
                }
    resuluts = []
    for s in ('split_8020','pass_kwargs'):
        result = functions['id3']( **{**arg_dict,**{'8020':eval(s)}} )
        result_tupple = (function_name,result['score'],result['TP'],result['TN'],result['FP'],result['FN'],s)
        resuluts.append(result_tupple) 
    columns = ('function','score','TP','TN','FP','FN','number of bins')
    return matrix_to_df(columns, resuluts)

'''
DDDDDDDDDDDDD                             iiii                                                               
D::::::::::::DDD                         i::::i                                                              
D:::::::::::::::DD                        iiii                                                               
DDD:::::DDDDD:::::D                                                                                          
  D:::::D    D:::::D rrrrr   rrrrrrrrr  iiiiiiivvvvvvv           vvvvvvv eeeeeeeeeeee    rrrrr   rrrrrrrrr   
  D:::::D     D:::::Dr::::rrr:::::::::r i:::::i v:::::v         v:::::vee::::::::::::ee  r::::rrr:::::::::r  
  D:::::D     D:::::Dr:::::::::::::::::r i::::i  v:::::v       v:::::ve::::::eeeee:::::eer:::::::::::::::::r 
  D:::::D     D:::::Drr::::::rrrrr::::::ri::::i   v:::::v     v:::::ve::::::e     e:::::err::::::rrrrr::::::r
  D:::::D     D:::::D r:::::r     r:::::ri::::i    v:::::v   v:::::v e:::::::eeeee::::::e r:::::r     r:::::r
  D:::::D     D:::::D r:::::r     rrrrrrri::::i     v:::::v v:::::v  e:::::::::::::::::e  r:::::r     rrrrrrr
  D:::::D     D:::::D r:::::r            i::::i      v:::::v:::::v   e::::::eeeeeeeeeee   r:::::r            
  D:::::D    D:::::D  r:::::r            i::::i       v:::::::::v    e:::::::e            r:::::r            
DDD:::::DDDDD:::::D   r:::::r           i::::::i       v:::::::v     e::::::::e           r:::::r            
D:::::::::::::::DD    r:::::r           i::::::i        v:::::v       e::::::::eeeeeeee   r:::::r            
D::::::::::::DDD      r:::::r           i::::::i         v:::v         ee:::::::::::::e   r:::::r            
DDDDDDDDDDDDD         rrrrrrr           iiiiiiii          vvv            eeeeeeeeeeeeee   rrrrrrr            
'''

# t test
#########
# id3
df_to_csv(create_t_test('id3', (1, 2, 3)), 'test_log/id3_t_test.csv')
# our_id3
df_to_csv(create_t_test('our_id3', (1, 2, 3)), 'test_log/our_id3_t_test.csv')


# k test
#########
# knn
df_to_csv(create_k_test('knn', (1, 2, 3)),'test_log/knn_k_test.csv')
# k means
df_to_csv(create_k_test('k_means', (1, 2, 3)),'test_log/k_means_k_test.csv')

# bins test
##################
# id3
df1 = create_bins_number_test( 'id3', (1, 2, 3))
# our id3
df2 = create_bins_number_test( 'our_id3', (1, 2, 3))
# naive bayes
df3 = create_bins_number_test( 'naive_bayes', (1, 2, 3))
# our naive bayes
df4 = create_bins_number_test( 'our_naive_bayes', (1, 2, 3))
# all to one csv
df_to_csv(pd.concat([df1,df2,df3,df4]), 'test_log/bins_number_test.csv')

# missing values test
###########################
# id3
df1 = create_nans_test( 'id3' )
# our id3
df2 = create_nans_test( 'our_id3')
# naive bayes
df3 = create_nans_test( 'naive_bayes')
# our naive bayes
df4 = create_nans_test( 'our_naive_bayes')
# knn 
df5 = create_nans_test( 'knn')
# k means
df6 = create_nans_test( 'k_means')
# all to one csv
df_to_csv(pd.concat([df1,df2,df3,df4,df5,df6]), 'test_log/missing_values_test.csv')

# bining strategy tests
###########################
# id3
df1 = create_bining_strategy_test( 'id3' )
# our id3
df2 = create_bining_strategy_test( 'our_id3')
# naive bayes
df3 = create_bining_strategy_test( 'naive_bayes')
# our naive bayes
df4 = create_bining_strategy_test( 'our_naive_bayes')
# all to one csv
df_to_csv(pd.concat([df1,df2,df3,df4]), 'test_log/binning_strategy_test.csv')

# 80/20 vs test and train
###########################
# id3
df1 = create_split_test( 'id3' )
# our id3
df2 = create_split_test( 'our_id3')
# naive bayes
df3 = create_split_test( 'naive_bayes')
# our naive bayes
df4 = create_split_test( 'our_naive_bayes')
# knn 
df5 = create_split_test('knn')
# k means
df6 = create_split_test('k_means')
# all to one csv
df_to_csv(pd.concat([df1,df2,df3,df4,df5,df6]), 'test_log/binning_strategy_test.csv')