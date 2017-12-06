# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:32:49 2017

@author: matia
"""

import numpy as np
def timeDilation(t,v):
    c=299792458
    NT=np.size(t)
    NV=np.size(v)
    T=np.zeros((NT,NV))
    for nt in range (NT):
        for nv in range (NV):
            T[nt,nv]=t[nt]/np.sqrt(1-v[nv]**2/c**2)
    return T