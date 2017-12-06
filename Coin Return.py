# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:40:07 2017

@author: matia
"""
import math
import numpy as np
def coinReturn(coinsInMachine,amount):
    x=amount
    coinsToReturn=np.array([])
    while x>=min(coinsInMachine)/2:
        coinIndex=np.max(np.where(coinsInMachine<=x))
        coinValue=coinsInMachine[coinIndex]
        coinsToReturn=np.append(coinsToReturn,coinValue)
        x=x-coinValue
    return coinsToReturn
                
    