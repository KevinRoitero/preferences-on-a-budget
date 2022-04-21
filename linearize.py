# Author: Alessandro Checco
# Tested with prefs = [('A','C','A'),('B','C','B'),('A','B','A'),('A','B','B')]
# and with prefs = [("A","B","A"), ("A","D","D"),("A","C","A"),("B","C","B")]
#
# USAGE:
# import linearize
# linearize.linearize([('A','C','A'),('B','C','B'),('A','B','A'),('A','B','B')])
# [['A', 'B'], ['C']]

import numpy as np
import pandas as pd
from choix import ilsr_pairwise
from itertools import groupby
from scipy.stats import rankdata


def linearize(prefs):
    pref_choix,n_items,lookup_dict,index_dict = convert_kevin_choix(prefs)
    #print(pref_choix)
    scores = ilsr_pairwise(n_items, pref_choix, alpha=0.001, initial_params=None, max_iter=200, tol=1e-08) #can we have an estimate on how confident we are on the scores? Need to use BradleyTerry2 from rpy2
    scores = scores + np.abs(np.min(scores))  #rendiamoli positivi
    scores = (scores/np.max(scores) * 1000).astype(int) #rendiamoli interi
    #print(scores)
    ranking_with_ties = rankdata(-scores,method='dense')-1
    rr = list(zip(ranking_with_ties,list(lookup_dict.values()),scores))
    rr = sorted(rr,key=lambda x:x[0])
    ranked_docs = []
    grouped_scores = []
    for k,g in groupby(rr,lambda x:x[0]):
        lev = []
        for i in list(g):
            lev.append(i[1])
        ranked_docs.append(lev)
        grouped_scores.append(i[2])
    return ranked_docs,grouped_scores

def convert_kevin_choix(prefs):
    pref_choix = []
    flattened = [item for sublist in prefs for item in sublist]
    unique_documents = np.unique(flattened)
    n_items=len(unique_documents)
    lookup_dict=dict((i,j) for i,j in enumerate(unique_documents))
    index_dict= dict((j,i) for i,j in enumerate(unique_documents))
    for i in prefs:
        pair = i[0:2]
        if pair[0]==i[2]: #correct order
            pref_choix.append( (index_dict[pair[0]],index_dict[pair[1]]))
        else: #reversed
            pref_choix.append( (index_dict[pair[1]],index_dict[pair[0]]))
    return pref_choix,n_items,lookup_dict,index_dict