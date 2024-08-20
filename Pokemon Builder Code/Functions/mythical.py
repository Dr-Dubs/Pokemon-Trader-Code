# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:39:28 2024

@author: jason
"""

'Mythicals Function'

def mythical(gen, game):
    
    if gen == 'Gen 1':
        # Structure: Species, Level, move1, move2, move3, move4
        poke1 = ['Mew', 5, 'Pound']
        party = [poke1]
        
    elif gen == 'Gen 2':
        poke1 = ['Celebi', 30, 'Heal Bell', 'Safeguard', 'Ancient Power', 
                 'Future Sight']
        poke2 = ['Mew', 5, 'Pound']
        poke3 = ['Mewtwo', 70, 'Psych Up', 'Future Sight', 'Mist', 'Psychic']
        poke4 = ['Celebi', 5, 'Leech Seed', 'Confusion', 'Heal Bell', 
                 'Recover']
        party = [poke1, poke2, poke3, poke4]


    return(party)