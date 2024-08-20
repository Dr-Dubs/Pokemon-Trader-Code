# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:57:38 2024

@author: jason
"""

'Choice Pokemon Function'

def choice(gen):
    
    if gen == 'Gen 1':
        # Structure: Species, Level
        poke1 = ['Hitmonlee', 30, 'Double Kick', 'Meditate']
        poke2 = ['Hitmonchan', 30, 'Comet Punch', 'Agility']
        poke3 = ['Omanyte', 30, 'Water Gun', 'Withdraw']
        poke4 = ['Kabuto', 30, 'Scratch', 'Harden']
        party = [poke1, poke2, poke3, poke4]
        
    elif gen == 'Gen 3':
        poke1 = ['Chikorita', 1, 'Growl', 'Tackle']
        poke2 = ['Cyndaquil', 1, 'Leer', 'Tackle']
        poke3 = ['Totodile', 1, 'Leer', 'Scratch']
        party = [poke1, poke2, poke3]


    return(party)