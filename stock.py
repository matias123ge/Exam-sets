# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:54:55 2017

@author: matia
"""

import numpy as np
def cumulativeStock(transactions):
    N=len(transactions)
    stock=np.zeros(N)
    currentstock=0
    for i in range (N):
        if transactions[i]==0:
            currentstock=0
        else:
            currentstock=currentstock+transactions[i]
        stock[i]=currentstock
    return stock