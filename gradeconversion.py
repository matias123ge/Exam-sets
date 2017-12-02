# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:10:06 2017

@author: matia
"""


def convertGrade (grade,scale):
    if scale=="7-point" :
        if grade==12:
            ECTSGrade="A"
        elif grade==10 :
            ECTSGrade="B"
        elif grade==7  :
            ECTSGrade="C"
        elif grade==4 :
            ECTSGrade="D"
        elif grade==2 :
            ECTSGrade="E"
        elif grade==0 :
            ECTSGrade="Fx"
        elif grade==-3 :
            ECTSGrade="F"
    else:
        if grade==13 or grade==11:
            ECTSGrade="A"
        elif grade==10 :
            ECTSGrade="B"
        elif grade==9 or grade==8  :
            ECTSGrade="C"
        elif grade==7 :
            ECTSGrade="D"
        elif grade==6 :
            ECTSGrade="E"
        elif grade==5 or grade==3 :
            ECTSGrade="Fx"
        elif grade==0 :
            ECTSGrade="F"
    return ECTSGrade