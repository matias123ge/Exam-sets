# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:23:17 2017

@author: Shady2
"""

import numpy as np
 
def acState(state, timeStamp):
 
    # Compute duration of states
    duration = np.diff(timeStamp)
     
    # Make zero stateTime vector
    stateTime = np.zeros(5)
     
    # Loop over states
    for s in range(5):
        # Compute total time in state
        stateTime[s] = np.sum(duration[state[:-1] == s])   
     
    return stateTime

        