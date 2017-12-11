# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:16:52 2017

@author: matia
"""
import math
import numpy as np
def normalWeight(h):
    wlow=math.ceil(18.5*h**2)
    whigh=math.floor(25*h**2)
    W=np.array([wlow,whigh])
    return W