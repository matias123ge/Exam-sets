# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:42:24 2017

@author: Shady2
"""

import numpy as np
def symmetrize(x):
    y=x+np.transpose(x)-np.diag(np.diag(x))
    return y