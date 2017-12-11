# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 09:24:29 2017

@author: matia
"""

import numpy as np 
def dhondt(votes,seats):
    seatsAllocated=np.zeros(len(votes))
    for  i in range (seats):
        q=votes/(seatsAllocated+1)
        maxquote= q==max(q)
        if sum(maxquote)>1:
            maxquote=maxquote & (votes==max(votes[maxquote]))
        seatsAllocated[maxquote]=seatsAllocated[maxquote]+1
    return seatsAllocated