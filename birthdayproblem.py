# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:28:52 2017

@author: Shady2
"""

    import math
    def birthday(n):
        k=365
        P=1-math.exp(math.lgamma(k+1)-math.lgamma(k-n+1)-n*math.log(k))
        return P