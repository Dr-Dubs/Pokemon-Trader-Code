# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 56:57:53 2024

@author: jason
"""

'Version Exclusives Function'

def VEs(gen, game):
    
    # Structure: Species, Level, move 5, move 2
    
    if gen == 'Gen 1':
        
        if game == 'Red':
            poke1 = ['Sandshrew', 5, 'Scratch']
            poke2 = ['Vulpix', 5, 'Ember', 'Tail Whip']
            poke3 = ['Meowth', 5, 'Scratch', 'Growl']
            poke4 = ['Bellsprout', 5, 'Vine Whip']
            poke5 = ['Magmar', 5, 'Smog', 'Leer', 'Ember']
            poke6 = ['Pinsir', 5, 'Vice Grip']
            
        elif game == 'Blue':
            poke1 = ['Ekans', 5, 'Wrap', 'Leer']
            poke2 = ['Oddish', 5, 'Absorb']
            poke3 = ['Mankey', 5, 'Scratch', 'Leer']
            poke4 = ['Growlithe', 5, 'Bite', 'Roar']
            poke5 = ['Scyther', 5, 'Quick Attack']
            poke6 = ['Electabuzz', 5, 'Quick Attack', 'Leer']
        
        
    elif gen == 'Gen 2':
        
        if game == 'Gold':
            poke1 = ['Vulpix', 5, 'Ember', 'Tail Whip']
            poke2 = ['Meowth', 5, 'Scratch', 'Growl']
            poke3 = ['Ledyba', 5, 'Tackle']
            poke4 = ['Delibird', 5, 'Present']
            poke5 = ['Skarmory', 5, 'Leer', 'Peck']
            poke6 = ['Phanpy', 5, 'Tackle', 'Growl']
        
        elif game == 'Silver':
            poke1 = ['Mankey', 5, 'Scratch', 'Leer']
            poke2 = ['Growlithe', 5, 'Bite', 'Roar']
            poke3 = ['Spinarak', 5, 'Poison Sting', 'String Shot']
            poke4 = ['Gligar', 5, 'Poison Sting']
            poke5 = ['Teddiursa', 5, 'Scratch', 'Leer']
            poke6 = ['Mantine', 5, 'Tackle', 'Bubble']


    party = [poke1, poke2, poke3, poke4, poke5, poke6]

    return(party)