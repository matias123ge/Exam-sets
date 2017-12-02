# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:03:23 2017

@author: matia
"""

import numpy as np
def cvrchecksum(cvr):
    list1=[int(i) for i in str(cvr)]
    weight=np.array([2,7,6,5,4,3,2])
    checksum=11-np.sum(list1*weight) % 11
    return checksum