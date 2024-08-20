# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:53:03 2024

@author: jason
"""

'Pokemon Builder'
'Built by Jason Schirck on 6/6/2024'

import time
import sys
sys.path.append('Functions')
from Starters import starters
from Converter import converter
from Output_File import file_editing
from version_exclusives import VEs
from mythical import mythical
from trader import trader
from other_gen import other_gen
from Custom import custom


gen = []
game = []
while game == []:
    # Step 1: Choose the generation (1-5)
    print('Choose Pokemon Generation:')
    print()
    print('Options:')
    print('Gen 1: Red, Blue, Yellow')
    print('Gen 2: Gold, Silver, Crystal')
    print('Gen 3: Ruby, Sapphire, Emerald, Fire Red, Leaf Green')
    print('Gen 4: Diamond, Pearl, Platinum, Heart Gold, Soul Silver')
    print('Gen 5: Black, White, Black 2, White 2')
    print()
    gen = input()
    
    
    # Step 2: Choose the trade to game
    if gen == 'Gen 1' or gen == '1':
        print()
        print('Choose physical game:')
        print()
        print('Options: ', gen)
        print('Red')
        print('Blue')
        print('Yellow')
        print('Green')
        print()
        game = input()
        
    elif gen == 'Gen 2' or gen == '2':
        print()
        print('Choose physical game:')
        print()
        print('Options: ', gen)
        print('Gold')
        print('Silver')
        print('Crystal')
        print()
        game = input()
        
    elif gen == 'Gen 3' or gen == '3':
        print()
        print('Choose physical game:')
        print()
        print('Options: ', gen)
        print('Ruby')
        print('Sapphire')
        print('Emerald')
        print('Fire Red')
        print('Leaf Green')
        print()
        game = input()
        
    elif gen == 'Gen 4'or gen == '4':
        print()
        print('Choose physical game:')
        print()
        print('Options: ', gen)
        print('Diamond')
        print('Pearl')
        print('Platinum')
        print('Heart Gold')
        print('Soul Silver')
        print()
        game = input()
        
    elif gen == 'Gen 5'or gen == '5':
        print()
        print('Choose physical game:')
        print()
        print('Options: ', gen)
        print('Black')
        print('White')
        print('Black 2')
        print('White 2')
        print()
        game = input()
        
    else:
        print()
        print('I am sorry. Either you have chosen an unsupported generation,')
        print('or you did not use the correct syntax.')
        print('Only generations 1-5 are supported at this time.')
        print('Please use the format: Gen #')
        print()
        time.sleep(10)


# Step 3: Choose a pokemon category
print()
print('Choose a pokemon list:')
print()
print('Options:')
print('Starters')
print('Version Exclusives')
print('Mythicals')
print('Choice (fossils, etc.)')
print('Other Gen')
print('Trading Dummy')
print('Custom')
print()
poke_list = input()


# Step 4: Create the pokemon in binary
if poke_list == 'Starters':
    party = starters(gen, game)

elif poke_list == 'Version Exclusives':
    party = VEs(gen, game)
    
elif poke_list == 'Mythicals':
    party = mythical(gen, game)
    
elif poke_list == 'Trading Dummy':
    party = trader(gen, game)
    
elif poke_list == 'Other Gen':
    party = other_gen(gen)

if poke_list == 'Custom':
    party_hex, poke_line_hex, trainerid, nickname_all = custom(gen)
else:
    party_hex, poke_line_hex, trainerid, nickname_all = converter(gen, party)
    
file_editing(gen, party_hex, poke_line_hex, trainerid, nickname_all)