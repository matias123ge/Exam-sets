# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:58:33 2017

@author: matia
"""

def industry(industryCode):
 
    # Replace wild-card "x" with zero. This works, because we can assume
    # that the given code always matches exactly one code range
    industryCode = industryCode.replace('x', '0')
 
    # Convert industry code string to number
    code = int(industryCode)
 
    # Match the code number to the industry name
    if code < 1000:
        industryName = 'Agriculture'
    elif code < 1500:
        industryName = 'Mining'
    elif code < 2000:
        industryName = 'Construction'
    elif code < 4000:
        industryName = 'Manufacturing'
    elif code < 5000:
        industryName = 'Transportation'
    elif code < 6000:
        industryName = 'Trade'
    elif code < 7000:
        industryName = 'Finance'
    elif code < 9000:
        industryName = 'Services'
    else:
        industryName = 'Public'
 
    return industryName