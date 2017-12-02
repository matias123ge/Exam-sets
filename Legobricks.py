# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:56:47 2017

@author: matia
"""


def buildLego(h,l,w):
    W=h*l*w
    for i in range(10000):
        if W*(i+1)>1000:
            bricks=i
            break
    return bricks