# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:44:10 2017

@author: Shady2
"""

import numpy as np

def matrixSearch(A,x):
    M,N=A.shape
    i=1
    j=N
    while A[i-1,j-1]!=x:
        if A[i-1,j-1]>x:
            j=j-1
        else:
            i=i+1
        if i>M or j<1:
            j=0
            i=0
            break
    index=np.array([i,j])
    return index