# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:42:04 2017

@author: matia
"""

import numpy as np 
def danceClass(v) :
    numberlef=np.sum(v==0)-np.sum(v==1)
    if len(v)>30: 
        s="invalid"
    elif len(v)<10:
        s="invalid"
    elif numberlef>3 or numberlef<-3:
        s="invalid"
    else:
        s="valid"
    return s
    