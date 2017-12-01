# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:01:40 2017

@author: Shady2
"""


def genderGuess(name):
    name.lower()
    if name[-1] in "aeiouy":
        if name.count("f")>=2:
            pFemale=0.35
        else:
            pFemale=0.87
    else:
        if name[0] in "k":
            pFemale=0.69
        else:
            pFemale=0.25
    return pFemale
            
            