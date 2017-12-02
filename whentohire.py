# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:35:41 2017

@author: matia
"""


def hireApplicant(skill, pay):
    x=skill
    y=pay
    if x<5: 
        say="No go" 
    if x>=5 and y>0.9*x+1: 
        say="Too expensive"
    if 5<=x<8 and y<=0.9*x+1:
        say="Hire"
    if x>=8 and 4<y<=0.9*x+1:
        say="Long term contract"
    if x>=8 and y<=4 :
        say="Unicorn"
    applicantZone=say
    return applicantZone