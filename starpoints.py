# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:56:08 2017

@author: matia
"""
import math
def starPoints(a,b,maxArea):
    for i in range (100000000000):
        if (i+1)*a*b*math.sin(math.pi/(i+1))>maxArea:
            n=i
            break
    return n
 
    