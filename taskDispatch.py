# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:21:06 2017

@author: matia
"""
import numpy as np
def taskDispatch(tasks,units):
    N=np.size(tasks)
    K=np.size(units)
    assignment=np.zeros(N)
    for k in range(K):
        for n in range(N):
            if assignment[n]==0:
                if units[k]>=tasks[n]:
                    assignment[n]=k+1
                    units[k]=units[k]-tasks[n]
    return assignment