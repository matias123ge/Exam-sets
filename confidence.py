# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:05:46 2017

@author: matia
"""

import numpy as np
def confidence(x):
    m=np.mean(x)
    s=(x-m)/(len(x)-1)
    s=np.linalg.norm(s)
    conf=np.array([m-s,m+s])
    return conf
#broken