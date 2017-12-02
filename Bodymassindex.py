# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:48:41 2017

@author: matia
"""


def classifyBMI(height,weight):
    b=weight/height**2
    if b<16:
        BMIGroup="Severely underweight"
    if 16 <= b < 18.5 :
        BMIGroup="Underweight"
    if 18.5 <= b < 25 :
        BMIGroup="Normal"
    if 25 <= b < 30 :
        BMIGroup="Overweight"
    if 30 <= b < 40 :
        BMIGroup="Obese"
    if 40 <=b:
        BMIGroup = "Severely obese" 
    return BMIGroup
