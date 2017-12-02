# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:21:44 2017

@author: matia
"""
import numpy as np
def sudokuCheck(sudokuBoard):
    check=0
    for i in range (9):
        if np.sum(sudokuBoard[i,:])!=45:
            check+=1
    for i in range (9):
        if np.sum(sudokuBoard[:,i])!=45:
            check+=1
    for i in range (3):
        for j in range (3):
            
           if np.sum(sudokuBoard[i*3:(i+1)*3,j*3:(j+1)*3])!=45:
               check+=1
    return check
            
    