# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:17:21 2017

@author: matia
"""

def capitalize(strin):
 
    # Define punctuation marks, upper and lower case letters
    marks = '.!?'
    lc = 'abcdefghijklmnopqrstuvwxyz'
    uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     
    strin = list(strin)
    strout = strin
 
    # True/false whether next character should be capitalized
    Caps = True
 
    # Loop over all characters
    for i in range(0, len(strin)):
        # Skip spaces
        if strin[i] is ' ':
            continue
         
        if Caps is True and lc.find(strin[i]) != -1:
            # Capitalize if character is a letter
            indx = lc.index(strin[i])
            strout[i] = uc[indx]
            # Stop capitalizing, when we have capitalized a character
            Caps = False
        elif marks.find(strin[i]) != -1:
            # Start capitalizing after we see a punctuation mark
            Caps = True
        else:
            Caps = False
                         
    strout = "".join(strout)
             
    return strout