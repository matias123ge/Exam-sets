# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:22:07 2017

@author: Shady2
"""


def alphaToPhone(alpha):
   alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   number="22233344455566677778889999"
   phone=""
   for i in range (len(alpha)):
       if alpha[i] in alphabet:
           phone=phone+number[alphabet.find(alpha[i])]
       else:
           phone=phone+alpha[i]
   return phone
            
    