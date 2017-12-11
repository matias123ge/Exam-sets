# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:12:38 2017

@author: matia
"""


def greenEyes(p1,p2):
    if p1=="brown" and p2=="brown":
        P=19 
    if p1=="brown" and p2=="blue" or p1=="blue" and p2=="brown" :
        P=0 
    if p1=="brown" and p2=="green" or p1=="green" and p2=="brown":
        P=38
    if p1=="blue" and p2=="blue":
        P=1
    if p1=="blue" and p2=="green" or p1=="green" and p2=="blue":
        P=50
    if p1=="green" and p2=="green":
        P=75 
    return P