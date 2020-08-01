'''
Author's: Belochitsky Oleg , Alfi Tal , Friza Ziv
IDs: 321192577, 204557052, 312196355
'''
import pandas as pd
import numpy as np
import random
from statistics import mode ,StatisticsError
'''
           __                              __     
          /  |                            /  |    
  ______  $$ |____    ______   __    __  _$$ |_   
 /      \ $$      \  /      \ /  |  /  |/ $$   |  
 $$$$$$  |$$$$$$$  |/$$$$$$  |$$ |  $$ |$$$$$$/   
 /    $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ | __ 
/$$$$$$$ |$$ |__$$ |$$ \__$$ |$$ \__$$ |  $$ |/  |
$$    $$ |$$    $$/ $$    $$/ $$    $$/   $$  $$/ 
 $$$$$$$/ $$$$$$$/   $$$$$$/   $$$$$$/     $$$$/  

This code is for supervised binning by entropy with
algorithem that relay on the concept of pure sets.

first we bin the data into pure sets
and then we adjusting the number of bins to the 
number of bins that required
by spliting wide bins (does not change the purty of them)
or by merging bins that :
    * first priority is to merge neighbors bins with same polarity 
    * secod priority is to merge neigbors bins with max size differeace
this way we making minimal damage to the entropy

useage:
This file can be used with 
'entropy_bining' function wich gets :
    dataframe, column name and number of bins
and returns:
    binned column and the bins 
'''
def bins_to_bin_edges(bins):
    '''
    get : bins
    return : tuple of bins edges 
    '''
    e1, e2 = tuple(zip(*bins))
    edges = (*e1,e2[-1])
    return edges


def bin_edges_to_bins(bin_edges):
    '''
    get : bin edges
    return : bin from that edges
    '''
    return tuple(zip(bin_edges, bin_edges[1:]))

def get_sorted_pairs(data,column):
    '''
    get : dataframe and column name
    retrun : tuple(tuple(value, classification ),....) **sorted**
    '''
    pairs = list(zip(data[column].tolist(),data['class'].tolist()))
    return tuple(sorted(pairs, key=lambda x: x[0]))

def get_classification_counts(sorted_pairs):
    '''
    get : tuple(tuple(value, classification ),....) **sorted**
    return : dict( (value:classification), ...)
             ,dict( (value:clasification count), ...)
    ''' 
    classifications = {}
    classificaton_counts = {}
    
    buffer = []
    cur = sorted_pairs[0][0]
    for i in range(len(sorted_pairs)):
        if(cur == sorted_pairs[i][0]):
            buffer.append(sorted_pairs[i][1])
        else:
            try:
                classifications[sorted_pairs[i][0]] = mode(buffer)
            except StatisticsError as e:
                classifications[sorted_pairs[i][0]] = 'yes' if bool(random.getrandbits(1)) else 'no'

            classificaton_counts[sorted_pairs[i][0]] = buffer.count(classifications[sorted_pairs[i][0]])
            buffer = []
            buffer.append(sorted_pairs[i][1])
            cur = sorted_pairs[i][0]

    return classifications, classificaton_counts

def create_prefect_bins(classifications, classification_counts ):
    '''
    get : dict( (value:classification), ... ),  dict( (value:clasification count), ...)
    return : tuple((value,value),...)
            , tuple(classification count, ...)
            , tuple(classification, ...)
    '''
    values,classif = tuple(zip(*tuple(sorted(classifications.items(), key=lambda x: x[0]))))

    bin_edges = [values[0]]
    bin_classif = []
    bin_weight = [] 

    cur = classif[0]
    weight = classification_counts[values[0]]
    for i in range(1,len(values)):
        if(cur != classif[i]):
            bin_edges.append(values[i-1])
            bin_classif.append(cur)
            bin_weight.append(weight)
            weight = classification_counts[values[i]]
            cur = classif[i]
        else:
            weight = weight + classification_counts[values[i]]
    
    last_edge = values[len(values) - 1]
    if last_edge != bin_edges[len(bin_edges) - 1]:
        bin_edges.append(last_edge)
        bin_classif.append(classif[len(classif) - 1])
        bin_weight.append(weight)

    bins = bin_edges_to_bins(bin_edges)
    return bins , bin_weight, bin_classif 

def split_bigest_bin(bins):
    '''
    spliting the widest bin in the middle
    '''
    ranges = tuple(y-x for x, y in bins)
    i = ranges.index(max(ranges))
    l = bins[i][0]
    r = bins[i][1]
    m = l + ranges[i]/2
    return (*bins[:i], (l, m), (m, r),  *bins[i+1:])

def split_bigest_n_times(bins, n):
    '''
    applying split n times
    '''
    while(n > 0):
        bins = split_bigest_bin(bins)
        n = n - 1
    return bins

def find_best_place_to_merge(bins, weights, polarity ):
    '''
    geting bing info
    returning index (index of the left side bin in the marge)
    for the marge acording to: 
        * first priority is to merge neighbors bins with same polarity
        * secod priority is to merge neigbors bins with max size differeace
    '''
    # first priority:
    for i in range(len(polarity)-1):
        if( polarity[i] == polarity[i+1]):
            return i

    # second priority
    bins_pairs = tuple(zip(bins,bins[1:])) 
    ratio = []
    for bin1,bin2 in bins_pairs:
        if (weights[bins.index(bin1)] < weights[bins.index(bin2)]):
            ratio.append( weights[bins.index(bin2)] /weights[bins.index(bin1)])
        else:
            ratio.append( weights[bins.index(bin1)] /weights[bins.index(bin2)])

    return ratio.index(max(ratio))


def merge_2_bins(bins, weights, polarity ):
    '''
    get: bins and info about the bins
    return: bins and info about the bins after mergeing two bins into one
    '''
    i = find_best_place_to_merge(bins, weights, polarity)

    # creating the new bins
    bin_edges = bins_to_bin_edges(bins)
    new_bins = bin_edges_to_bins((*bin_edges[:i+1],*bin_edges[i+2:]))

    # updating the weights
    if( polarity[i]==polarity[i+1]):
        new_weight = weights[i] + weights[i+1]
    else:
        new_weight = weights[i] if (weights[i] > weights[i+1]) else  weights[i+1]
    new_weights = (*weights[:i], new_weight  ,*weights[i+2:])

    # updating the polarity
    new_polarity = polarity[i] if (weights[i] > weights[i+1]) else  polarity[i+1]
    new_polaritys = (*polarity[:i], new_polarity  ,*polarity[i+2:]) 
    return new_bins, new_weights, new_polaritys
    
def merge_bins_n_times(bins, weights, polarity, n):
    '''
    get : bins and info about them
    return : bins that been megred at specific locations n times
    '''
    while n > 0:
        bins, weights, polarity = merge_2_bins(bins, weights, polarity )
        n = n - 1
    return bins

def make_corect_number_of_bins(bins, weights, polarity, number_of_bins ):
    '''
    get : correct bins and info about them with thre requaired number of bins
    return : bins with required amount
    '''
    dif = number_of_bins - len(bins)
    if(dif > 0):
        corect_bins = split_bigest_n_times(bins, dif)
    elif(dif < 0):
        corect_bins = merge_bins_n_times(bins, weights, polarity , -dif)
    else:
        corect_bins = bins
    return corect_bins 

# entropy binning
def entropy_bining(data, column, number_of_bins):
    # checking classification of each value + classification counts
    classification, classification_counts = get_classification_counts(get_sorted_pairs(data,column))
    # create ideal bin      
    # ideal bins have pure classification( yes / no ) here called 'polarity'
    # ideal bins have weight ( the number of observation in the bin)
    bins, weights, polarity = create_prefect_bins(classification, classification_counts)
    # make the corect number of bins from the ideal bins
    corect_bins = make_corect_number_of_bins(bins, weights, polarity, number_of_bins )
    # apply the binning to the column cut the columns
    bin_edges = bins_to_bin_edges(corect_bins)

    if ( corect_bins[0][0]==corect_bins[0][1]): # if first bin is [1-1]
        bin_edges = (-float('inf'),*bin_edges[:-1], float('inf'))
    else:
        bin_edges = (-float('inf'),*bin_edges[1:-1], float('inf'))
    labels = np.arange(len(corect_bins))
    binned_column,bins = pd.cut(np.array(data[column]), bins=bin_edges, include_lowest=True, labels=labels, duplicates='drop', retbins=True)
    return binned_column, bins 
