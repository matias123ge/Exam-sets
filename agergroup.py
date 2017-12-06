# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:43:57 2017

@author: matia
"""

import numpy as np
def computeAgeGroup(age):
    agegrp=np.array(["Infant","Toddler","Child","Teenager","Adult"])
    if age<1:
        ageGroup=agegrp[0]
    elif 1<=age<3:
        ageGroup=agegrp[1]
    elif 3<=age<13:
        ageGroup=agegrp[2]
    elif 13<=age<20:
        ageGroup=agegrp[3]
    else:
        ageGroup=agegrp[4]
    return ageGroup