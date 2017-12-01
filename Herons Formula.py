# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:04:24 2017

@author: Shady2
"""

import math
def trianglearea(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        p=0.5*(a+b+c)
        A=math.sqrt(p*(p-a)*(p-b)*(p-c))
    else: 
        A=0
    return A
