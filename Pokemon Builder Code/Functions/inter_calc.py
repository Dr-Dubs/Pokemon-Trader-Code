# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:28:06 2024

@author: jason
"""

import math

def inter_calc(base, DV, stat_exp, level, gen, IV, EV):
    
    if gen == 'Gen 1' or gen == 'Gen 2':
    
        calc1 = math.floor(math.ceil(math.sqrt(stat_exp))/4)
        calc2 = math.floor( (((base+DV)*2 + calc1)*level)/100 )
        
    else:
        
        calc1 = math.floor(EV/4)
        calc2 = math.floor( ((2*base+IV+calc1)*level)/100 )
    
    
    return(calc2)