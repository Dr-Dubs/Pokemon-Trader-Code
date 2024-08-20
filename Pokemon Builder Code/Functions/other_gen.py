# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:39:28 2024

@author: jason
"""

'Other Generation Function'

def other_gen(gen):
    
    if gen == 'Gen 2':
        
        print()
        print('Choose a pokemon list:')
        print()
        print('Set 1: Gen 1 Starters and Legendary Birds')
        print('Set 2: Gen 1 Fossil Pokemon')
        print()
        set_num = input()
        
        if set_num == 'Set 1' or set_num == '1':
            # Structure: Species, Level, move1, move2, move3, move4, item?
            poke1 = ['Bulbasaur', 5, 'Tackle', 'Growl']
            poke2 = ['Charmander', 5, 'Scratch', 'Growl']
            poke3 = ['Squirtle', 5, 'Tackle', 'Tail Whip']
            poke4 = ['Articuno', 50, 'Peck', 'Ice Beam']
            poke5 = ['Zapdos', 50, 'Thunder Shock', 'Drill Peck']
            poke6 = ['Moltres', 50, 'Peck', 'Fire Spin']
            party = [poke1, poke2, poke3, poke4, poke5, poke6]
        
        else:            
            poke1 = ['Omanyte', 30, 'Water Gun', 'withdraw']
            poke2 = ['Kabuto', 30, 'Scratch', 'Harden']
            party = [poke1, poke2]

    return(party)