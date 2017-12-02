# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:25:30 2017

@author: matia
"""


def nextleapyear(y):
 
    # Is current year a leap year?
    isLeapYear = False
 
    # Initial year
    l = y
 
    # Loop until we find a leap year
    while isLeapYear == False:
        # Go to next year
        l = l+1
 
        # Leap year if divisible by four
        if l%4 == 0:
            isLeapYear = True
 
            # But not leap year if divisible by one hundred
            if l%100 == 0:
                isLeapYear = False
 
                # Except if also divisible by four hundred
                if l%400 == 0:
                    isLeapYear = True
             
    return l