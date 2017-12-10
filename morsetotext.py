# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:04:36 2017

@author: Shady2
"""

import numpy as np
 
def morseToText(morseCode):
 
    # Define Morse alphabet including space character
    morseAlphabet = np.array([
        ".-","-...","-.-.","-..",".","..-.","--.","....","..",
        ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
        "...","-","..-","...-",".--","-..-","-.--","--..",""])
     
    # Define normal alphabet including space character
    AZAlphabet = np.array([
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N",
        "O","P","Q","R","S","T","U","V","W","X","Y","Z"," "])
     
    # Initialize empty text
    text = ""
     
    # Extract tokens
    tokens = morseCode.split(" ")
 
    # Loop over each token
    for token in tokens:
        # Convert token to letter
        letter = AZAlphabet[morseAlphabet==token]
        # Append to text
        text += letter[0]
         
    return text