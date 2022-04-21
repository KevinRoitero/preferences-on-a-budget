#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import scipy as sp
import itertools
import warnings
warnings.filterwarnings('ignore')


# In[9]:



def comp_number_of_occur(elem, lista):
    number_times_occur = np.sum([ 1 if elem in x else 0 for x in lista ])
    return number_times_occur

def comp_number_of_wins(elem, lista):
    number_times_occur = np.sum([1 if ((elem in x) and (elem in x[2])) else 0 for x in lista ])
    return number_times_occur

def comp_number_of_lose(elem, lista):
    number_times_occur = np.sum([1 if ((elem in x) and (elem not in x[2])) else 0 for x in lista ])
    return number_times_occur

def comp_winlose(lista):
    unique_elements = set(itertools.chain.from_iterable(lista))
    res_dict = {
                elem:{
                    'occur': comp_number_of_occur(elem, lista),
                    'win': comp_number_of_wins(elem, lista),
                    'lose': comp_number_of_lose(elem, lista)
                }
                for elem in unique_elements
               }
    return res_dict

def sort_by_wins(res):
    get_max_occur = np.max([res[x]['occur'] for x in res])
    final = []
    for i in range(0,get_max_occur+1):
        toapp = [elem  for elem in res if (res[elem]['win'] == i) ]
        final.append(toapp)
    final = [elem for elem in final if elem != []]
    final = final[::-1]
    return final

# prefs = [
#     ("A","B","A"),
#     ("A","C","A"), # ("A","C","C") # per incongruenze
#     ("A","D","D"),
#     ("B","C","B")
# ]

# res = comp_winlose(prefs)
# print(res)
# res = sort_by_wins(res)
# print(res)



# In[ ]:





# In[ ]:




