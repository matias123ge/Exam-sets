# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:06:06 2017

@author: matia
"""

import numpy as np 
def polygonarea(x,y):
    determinants=0
    for i in range (len(x)-1):
        d=x[i]*y[i+2]-y[i]*x[i+1]
        determinants=determinants+d
    A=1/2*determinants
    return A