# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:19:47 2017

@author: matia
"""
import math
import numpy as np
def similarityMatrix(x,y,delta):
    d=delta
    xN=len(x)
    yN=len(y)
    matrix=np.zeros((xN,yN))
    for i in range (xN):
        for u in range (yN):
            s1=math.exp(-d*((x[i]-y[u])**2))
            matrix[i,u]=s1
            S=matrix
    return S