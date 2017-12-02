# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:48:06 2017

@author: matia
"""
import numpy as np
def averagedB(M):
    [row,col]=np.where(M>70)
    M=np.delete(M,row,axis=0)
    averageM=np.mean(M,0)
    return averageM
            