# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:30:20 2017

@author: matia
"""

import numpy as np
import math
def weekday(d,m,y):
    month=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    Car=np.array([6,2,2,5,0,3,5,1,4,6,2,4])
    for i in range (12):
        if m==month[i]:
            C=Car[i]
    w=(d+C+y+math.floor(y/4))%7
    weekday=np.array(["Sun","Mon","Tue","Wed","Thu","Fri","Sat"])
    name=weekday[w]
    return name
            