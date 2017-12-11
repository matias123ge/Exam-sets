# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:22:53 2017

@author: matia
"""
import numpy as np 
def bestBuy(p,m):
    n=0
    while n<np.size(p) and m>=p[n]:
        m=m-p[n]
        n=n+1
    return n