# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:30:33 2024

@author: jason
"""

import math

def exp_calc(gen, level, cat):    
        
    if cat == 'Fast':
        exp = 4/5*level**3
        
    elif cat == 'Medium Fast':
        exp = level**3
        
    elif cat == 'Medium Slow':
        exp = 6/5*level**3 - 15*level**2 + 100*level - 140
        
    elif cat == 'Slow':
        exp = 5/4*level**3
        
    elif cat == 'Erratic':
        if level < 50:
            exp = level**3*(100 - level)/50
            
        elif 50 <= level < 68:
            exp = level**3*(150 - level)/100
            
        elif 68 <= level < 98:
            exp = level**3*math.floor( (1911 - 10*level)/3 )/500
            
        else:
            exp = level**3*(160 - level)/100
            
    else: 
        if level < 15:
            exp = level**3*( math.floor((level+1)/3)+24 )/50
            
        elif 15 <= level < 36:
            exp = level**3*(level + 14)/50
            
        else:
            exp = level**3*(math.floor(level/2) + 32)/50
            
    
    exp = int(exp)
    if gen == 'Gen 1' or gen == 'Gen 2':    
        
        'Gen 1 exp hex is 3 bytes'
        exp_hex = [hex(exp//256**2), hex(exp%256**2//256), hex(exp%256**2%256)]
    
        
    elif gen == 'Gen 3':
        
        'Gen 3 exp (4 bytes)'
        
        exp_hex = [hex(exp%65536), hex(exp//65536)]
        
    return(exp_hex)