# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:52:11 2017

@author: matia
"""

import numpy as np
 
def approximatepi(N):
 
    # Create grid of x,y coordinates
    x,y = np.meshgrid(np.linspace(1.0/(2*N), 1-1.0/(2*N), N),np.linspace(1.0/(2*N), 1-1.0/(2*N), N))
 
    # Count number of points within circle
    nInCircle = np.sum((x**2 + y**2) < 1.0);
 
    # Compute approximation of pi
    val = nInCircle/float(N**2) * 4
 
    return val