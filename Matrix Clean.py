# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:11:47 2017

@author: matia
"""

import numpy as np
def matrixCleanup(M):
    lol=~np.any(M==0,axis=1)
    lel=~np.any(M==0, axis=0)
    M=M[lol,:]
    M=M[:,lel]
    return M