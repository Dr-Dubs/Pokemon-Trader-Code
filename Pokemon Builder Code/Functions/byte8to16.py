# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:45:37 2024

@author: jason
"""

def byte8to16(a, b):
    
    if len(b) == 4:
        ab = a + b[2:4]
    else:
        ab = a + '0' + b[2]
        
    return(ab)