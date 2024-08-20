# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:39:28 2024

@author: jason
"""

'Trader Dummy Function'

def trader(gen, game):
    
    if gen == 'Gen 1':
        # Structure: Species, Level, move1, move2, move3, move4, item?
        poke1 = ['Mew', 5, 'Pound']
        party = [poke1]
        
    elif gen == 'Gen 2':
        poke1 = ['Rattata', 5, 'Tackle', 'Tail Whip']
        item1 = 'Water Stone'
        party = [poke1]


    return(party)