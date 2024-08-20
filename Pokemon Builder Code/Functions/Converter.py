# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:14:50 2024

@author: jason
"""

'Pokemon Conversion Function'

from Gen1 import gen1_converter
from Gen2 import gen2_converter
from Gen3 import gen3_converter

def converter(gen, party):
      
    if gen == 'Gen 1':
        
        party_hex, poke_line_hex, trainerid, nickname = gen1_converter(gen, party)

    elif gen == 'Gen 2':
        
        party_hex, poke_line_hex, trainerid, nickname = gen2_converter(gen, party)
        
    else:

        party_hex, poke_line_hex, trainerid, nickname = gen3_converter(gen, party)     
        
            
    return(party_hex, poke_line_hex, trainerid, nickname)