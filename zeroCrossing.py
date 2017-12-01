# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:30:20 2017

@author: Shady2
"""

import numpy as np 
def zeroCrossing(signal):
 
    # Compute signal sign
    signal_sign = np.sign(signal)
 
    # Compute number of zero crossings
    count = np.sum(signal_sign[1:] != signal_sign[0:-1])
 
    return count
    
