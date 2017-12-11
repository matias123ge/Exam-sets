# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:52:41 2017

@author: matia
"""
import numpy as np 
def survivalTemperature(M,g):
    #Definer outer ranges: 
        if any(M>500) or any(M<50) or any(g<0.04) or any(g>0.45):
            T="RangeError"
        else: 
            #Calculate values using np.outer, which returns the matrix shape we want (more practical than double loop)
            intermediate=np.outer((0.9*M-12),((g+0.95)/(27.8*g)))
            T=36-intermediate
        return T