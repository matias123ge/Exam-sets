# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:20:08 2017

@author: matia
"""

import numpy as np
 
def nBest(allValues, N):
    # Sort the values in the array
    sortedValues = np.sort(allValues)
     
    # Get the value of the Nth largest
    NthLargest = sortedValues[np.size(allValues) - N]
 
    # Return the N largest values
    bestValues = allValues[allValues >= NthLargest]
 
    return bestValues