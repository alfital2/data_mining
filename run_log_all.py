
from start import get_result
import pandas as pd
import numpy as np

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
    like file opening functions, csv creating function.
    
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
DEFAULT_8020 = 'yes'
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
        result = get_result(function_name,**{**arg_dict, **{'tolorance': t}})
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
        result = get_result(function_name, **{**arg_dict,**{'k':k}})
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
        print(b)
        result = get_result(function_name, **{**arg_dict,**{'number_of_bins':b}})
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
        result = get_result(function_name, **{**arg_dict,**{'missing_values':s}})
        result_tupple = (function_name, result['score'],result['TP'],result['TN'],result['FP'],result['FN'],s)
        resuluts.append(result_tupple) 
    columns = ( 'function', 'score','TP','TN','FP','FN','dealing with nans strategy')
    return matrix_to_df(columns, resuluts)


# binning strategy test
def create_bining_strategy_test(function_name):
    arg_dict = {'test': DEFAULT_TEST,
                'train': DEFAULT_TRAIN,
                'structure': DEFAULT_STRUCTURE,
                'tolorance': DEFAULT_TOLORANCE,
                'k': DEFAULT_K,
                'number_of_bins': DEFAULT_NUMBER_OF_BINS,
                'bin_type': DEFAULT_BIN_TYPE,
                'missing_values': DEFAULT_MISSING_VALUES,
                '8020': DEFAULT_8020
                }
    resuluts = []
    for strategy in ['equal_width', 'equal_frequency', 'entropy']:
        result = get_result(
            function_name, **{**arg_dict, **{'bin_type': strategy}})
        result_tupple = (function_name, result['score'], result['TP'], result['TN'], result['FP'], result['FN'], strategy)
        resuluts.append(result_tupple)
    columns = ('function', 'score', 'TP', 'TN', 'FP', 'FN', 'strategy')
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
    for s in ('yes','no'):
        result = get_result(function_name, **{**arg_dict,**{'8020':s}})
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
df_to_csv(create_t_test('id3', tuple(i for i in range(1,100))), 'test_log/id3_t_test.csv')
print('finished id3 t test')
# our_id3
df_to_csv(create_t_test('our_id3',tuple(i for i in range(1,10))), 'test_log/our_id3_t_test.csv')
print('finished our id3 t test')


# k test
#########
# knn
df_to_csv(create_k_test('knn', tuple(i for i in range(1,50))),'test_log/knn_k_test.csv')
print('finished knn k test')
# k means
df_to_csv(create_k_test('k_means', tuple(i for i in range(1,50))),'test_log/k_means_k_test.csv')
print('finished kmeans k test')

# bins test
##################
# id3
bins_amouns = tuple( i for i in range(5,30,5))
df1 = create_bins_number_test( 'id3', bins_amouns)
print('finished id3 bins test')
# our id3
df2 = create_bins_number_test( 'our_id3',  bins_amouns)
print('finished our id3 bins test')
# naive bayes
df3 = create_bins_number_test( 'naive_bayes', bins_amouns)
print('finished nb bins test')
# our naive bayes
df4 = create_bins_number_test( 'our_naive_bayes', bins_amouns)
print('finished our nb bins test')
# all to one csv
df_to_csv(pd.concat([df1,df2,df3,df4]), 'test_log/bins_number_test.csv')

# missing values test
###########################
# id3
df1 = create_nans_test( 'id3' )
print('finished id3 nans test')
# our id3
df2 = create_nans_test( 'our_id3')
print('finished our id3 nans test')
# naive bayes
df3 = create_nans_test( 'naive_bayes')
print('finished nb nans test')
# our naive bayes
df4 = create_nans_test( 'our_naive_bayes')
print('finished our nb nans test')
# knn 
df5 = create_nans_test( 'knn')
print('finished knn nans test')
# k means
df6 = create_nans_test( 'k_means')
print('finished k means nans test')
# all to one csv
df_to_csv(pd.concat([df1,df2,df3,df4,df5,df6]), 'test_log/missing_values_test.csv')

# bining strategy tests
###########################
# id3
df1 = create_bining_strategy_test( 'id3' )
print('id3 binning type test')
# our id3
df2 = create_bining_strategy_test( 'our_id3') 
print('our id3 binning type test')
# naive bayes
df3 = create_bining_strategy_test( 'naive_bayes')
print('nb binning type test')
# our naive bayes
df4 = create_bining_strategy_test( 'our_naive_bayes') 
print('our nb binning type test')
# all to one csv
df_to_csv(pd.concat([df1,df2,df3,df4]), 'test_log/binning_strategy_test.csv')

# 80/20 vs test and train
###########################
# id3
df1 = create_split_test( 'id3' )
print('8020 vs test test id3')
# our id3
df2 = create_split_test( 'our_id3')
print('8020 vs test test our id3')
# naive bayes
print('8020 vs test test nb')
df3 = create_split_test( 'naive_bayes')
# our naive bayes
df4 = create_split_test( 'our_naive_bayes')
print('8020 vs test test our nb')
# knn 
df5 = create_split_test('knn')
print('8020 vs test test knn')
# k means
df6 = create_split_test('k_means')
print('8020 vs test test kmeans')
# all to one csv
df_to_csv(pd.concat([df1,df2,df3,df4,df5,df6]), 'test_log/8020_vs_test_test.csv')
