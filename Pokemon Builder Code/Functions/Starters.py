# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:14:19 2024

@author: jason
"""

'Starters Function'

def starters(gen, game):
    
    if gen == 'Gen 1':
        # Structure: Species, Level
        poke1 = ['Bulbasaur', 5, 'Tackle', 'Growl']
        poke2 = ['Charmander', 5, 'Scratch', 'Growl']
        poke3 = ['Squirtle', 5, 'Tackle', 'Tail Whip']
        
    elif gen == 'Gen 2':
        poke1 = ['Chikorita', 5, 'Growl', 'Tackle']
        poke2 = ['Cyndaquil', 5, 'Leer', 'Tackle']
        poke3 = ['Totodile', 5, 'Leer', 'Scratch']
        
    elif gen == 'Gen 3':
        if game == 'Ruby' or game == 'Sapphire' or game == 'Emerald':
            poke1 = ['Treecko', 5, 'Pound', 'Leer']
            poke2 = ['Torchic', 5, 'Scratch', 'Growl']
            poke3 = ['Mudkip', 5, 'Tackle', 'Growl']
        
        else:
            poke1 = ['Bulbasaur', 5, 'Tackle']
            poke2 = ['Charmander', 5, 'Scratch', 'Growl']
            poke3 = ['Squirtle', 5, 'Tackle', 'Tail Whip']


    party = [poke1, poke2, poke3]

    return(party)