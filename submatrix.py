# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:32:24 2017

@author: matia
"""

import numpy as np 
def submatrix(M,r,c):
    if 1<=r<=len(M):
        M=np.delete(M,r-1,0)
    if 1<=c<=len(M[0]):
        M=np.delete(M,c-1,1)
    S=M
    return S
        