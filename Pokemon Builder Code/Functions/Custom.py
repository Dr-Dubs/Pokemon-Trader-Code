# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:19:16 2024

@author: jason
"""

import pandas as pd
from Stat_Calculator import stat_calc
import random
from character_encoding import text_hex
from exp_calculator import exp_calc

def custom(gen):
    
    party_hex = []
    nickname_all = []
    comma = ', '
    end = '\n'
    number_poke = hex(1)
    poke_line_hex = str(number_poke) + comma
    
    if gen == 'Gen 2':
        data_fold = 'Data/Gen 2/'
    
    
    df_species = pd.read_csv(data_fold + 'Pokemon_Species.txt', 
                             sep = '\t', header = 0,
                             names = ['HEX', 'DEC', 'MS', 'Name', 
                                       'Type 1', 'Type 2'])
    
    df_stats = pd.read_csv(data_fold + 'Base_Stats.txt', sep = '\t', 
                             header = 0, 
                             names = ['Dex', 'Sprite', 'Name', 'HP', 
                                       'Att', 'Def', 'Spec_Att', 'Spec_Def', 
                                       'Speed', 'Total', 'Avg'])
    
    df_moves = pd.read_csv(data_fold + 'Move_List.txt', sep = '\t', 
                             header = 0, 
                             names = ['Dec', 'Name', 'Type', 'Category', 
                                      'PP', 'Power', 'Accuracy', 'Gen'])
    
    df_exp = pd.read_csv(data_fold + 'Exp_Categories.txt', sep = '\t', 
                             header = 0, 
                             names = ['Dec', 'Sprite', 'Name', 'Category'])
    
    df_gender = pd.read_csv(data_fold + 'Gender Ratio.txt', sep = '\t', 
                             header = 0, 
                             names = ['Name', 'GR'])
    
    df_item = pd.read_csv(data_fold + 'Item_List.txt', sep = '\t', 
                             header = 0, 
                             names = ['DEC', 'HEX', 'Item', 'Image', 'Bag Pocket'])
    
    
    'Pokemon Species'
    print()
    print('Enter a Pokemon name:')
    print()
    poke_name = input()
    
    
    'Level'
    print()
    print('Enter level (1-100):')
    print()
    level = int(input())
    
    
    'Moves'
    moves_str = []
    
    for i in range(0, 4):
        print()
        print('Enter move', i+1, ':')
        print()
        print('If no more moves desired, enter 0')
        move = input()
        
        if move == '0':
            break
        else:
            moves_str.append(move)
    
    moves = [0, 0, 0, 0]
    moves_PP = [0, 0, 0, 0]
    for i in range(0, len(moves_str)):
        for j in range(0, len(df_moves)):
            if df_moves.loc[j, 'Name'] == moves_str[i]:
                moves[i] = df_moves.loc[j, 'Dec']
                moves_PP [i] = df_moves.loc[j, 'PP']
                break
    
    
    'Shininess'
    print()
    print('Shiny? Y or N:')
    print('Note: DVs cannot be edited (Gen 2)')
    print()
    shiny = input()
    
    if shiny == 'Y':
        if gen == 'Gen 2':
            att_DV = 15         # Options: 2, 3, 6, 7, 10, 11, 14, 15
            def_DV = 10
            speed_DV = 10
            spec_DV = 10
            
            
    'Gender'
    print()
    print('Choose Pokemon gender (M or F):')
    print('Note: Some pokemon (Ex: Staryu) are genderless')
    print('Note: For Gen 2 pokemon, the attack DV determines gender')
    print()
    gender = input()
    
    if gen == 'Gen 2':
        for i in range(0, len(df_gender)):
            if df_gender.loc[i, 'Name'] == poke_name:
                gender_ratio = df_gender.loc[i, 'GR']
        
        if gender_ratio == 0.125:
            if gender == 'M':
                att_DV = 15
            else:
                att_DV = 1
                
        elif gender_ratio == 0.25:
            if gender == 'M':
                att_DV = 15
            else:
                att_DV = 3
           
        elif gender_ratio == 0.5:
            if gender == 'M':
                att_DV = 15
            else:
                att_DV = 7
                
        elif gender_ratio == 0.25:
            if gender == 'M':
                att_DV = 15
            else:
                att_DV = 11
                
        else:
            att_DV = 15
        
    
    'IVs/DVs'
    if gen == 'Gen 1' or gen == 'Gen 2':
        if shiny == 'N':
            print()
            print('Random DVs or Custom DVs?')
            print()
            print('Type Random or Custom:')
            print('Note: the Pokemon gender is determined from the Attack DV')
            print('The maximum possible value is chosen for each gender')
            DV_type = input()
        else:
            DV_type = 'Shiny'
        
    elif gen == 'Gen 3':
        print()
        print('Random IVs or Custom IVs?')
        print()
        print('Type Random or Custom:')
        print()
        IV_type = input()
        
    if DV_type == 'Custom':
        if gen == 'Gen 1' or gen == 'Gen 2':
            if shiny == 'Y':
                print()
                print('Shiny Pokemon have specific DVs in Gen 2.')
                print('To select DVs, start over and chosen non-shiny Pokemon')
                print()
            
            else:                
                print()
                print('Enter Defense DV (0-15):')
                print()
                def_DV = input()
                
                print()
                print('Enter Speed DV (0-15):')
                print()
                speed_DV = input()
                
                print()
                print('Enter Special DV (0-15):')
                print()
                spec_DV = input()
    else:
        if gen == 'Gen 1' or gen == 'Gen 2' and shiny == 'N':
            att_DV = random.randrange(16)
            def_DV = random.randrange(16)
            speed_DV = random.randrange(16)
            spec_DV = random.randrange(16)
    
    if gen == 'Gen 1' or gen == 'Gen 2':
        HP_DV = 8*(att_DV%2) + 4*(def_DV%2) + 2*(speed_DV%2) + spec_DV%2
        DV = [HP_DV, att_DV, def_DV, speed_DV, spec_DV, spec_DV] 
        DV1 = int('{0:04b}'.format(att_DV) + '{0:04b}'.format(def_DV), 2)
        DV2 = int('{0:04b}'.format(speed_DV) + '{0:04b}'.format(spec_DV), 2)
        
        
    'EVs'
    print()
    print()
    print('No EVs or Custom EVs?')
    print()
    print('Type None or Custom:')
    EV_type = input()
     
    if EV_type == 'Custom':
        if gen == 'Gen 1' or gen == 'Gen 2':
            print()
            print('Enter HP EV (0-65535):')
            print()
            HP_EV = int(input())
            
            print()
            print('Enter Attack EV (0-65535):')
            print()
            att_EV = int(input())
            
            print()
            print('Enter Defense EV (0-65535):')
            print()
            def_EV = int(input())
            
            print()
            print('Enter Speed EV (0-65535):')
            print()
            speed_EV = int(input())
            
            print()
            print('Enter Special EV (0-65535):')
            print()
            spec_EV = int(input())
            
    else:
        HP_EV = 0
        att_EV = 0
        def_EV = 0
        speed_EV = 0
        spec_EV = 0
        
    stat_exp = [HP_EV, att_EV, def_EV, speed_EV, spec_EV, spec_EV]
         
     
    'Friendship'
    print()
    print('Enter friendship (0-255):')
    print('Note: Friendship evolutions occur at 220+')
    print()
    friend = input()
    friend = hex(int(friend))
    
    
    'Pokerus'
    print()
    print('Pokerus? (Y or N):')
    print()
    pokerus = input()
    if pokerus == 'Y':
        rus = hex(244)
    else:
        rus = hex(0)
        
        
    'Held Item'
    print()
    print('Enter a held item or 0 for none:')
    print()
    held = input()
    
    if held == '0':
        item = hex(0)
        
    else:
        for i in range(0, len(df_item)):
            if df_item.loc[i, 'Item'] == held:
                item = df_item.loc[i, 'DEC']
                item = hex(int(item))
            
     
        
    'Base Stats'
    for i in range(0, len(df_stats)):
        if df_stats.loc[i, 'Name'] == poke_name:
            base = [df_stats.loc[i, 'HP'], df_stats.loc[i, 'Att'], 
                    df_stats.loc[i, 'Def'], df_stats.loc[i, 'Speed'], 
                    df_stats.loc[i, 'Spec_Att'], df_stats.loc[i, 'Spec_Def']]
            
    'Species'
    for i in range(0, len(df_species)):
        if df_species.loc[i, 'Name'] == poke_name:
            species = df_species.loc[i, 'DEC']
            species = hex(int(species))   
        
    'Stat Calculator'
    stats = stat_calc(gen, level, base, DV, stat_exp, 0, 0, 0)
            
    'Exp'
    for i in range(0, len(df_exp)):
        if df_exp.loc[i, 'Name'] == poke_name:
            exp_cat = df_exp.loc[i, 'Category']
            break
    
    'Stats'
    # item = hex(0)
    mv1 = hex(moves[0])
    mv2 = hex(moves[1])
    mv3= hex(moves[2])
    mv4 = hex(moves[3])
    OT = [hex(0), hex(0)]
    exp = exp_calc(gen, level, exp_cat)
    EV_HP = [hex(HP_EV//256), hex(HP_EV%256)]
    EV_att = [hex(att_EV//256), hex(att_EV%256)]
    EV_def = [hex(def_EV//256), hex(def_EV%256)]
    EV_speed = [hex(speed_EV//256), hex(speed_EV%256)]
    EV_spec = [hex(spec_EV//256), hex(spec_EV%256)]
    IV = [hex(DV1), hex(DV2)]
    mv1PP = hex(moves_PP[0])
    mv2PP = hex(moves_PP[1])
    mv3PP= hex(moves_PP[2])
    mv4PP = hex(moves_PP[3])
    # friend = hex(70)
    # rus = hex(0)
    caught = [hex(0), hex(0)]
    level = hex(int(level))
    status = hex(0)
    unused = hex(0)
    HP_curr = [hex(stats[0]//256), hex(stats[0]%256)]
    HP_max = [hex(stats[0]//256), hex(stats[0]%256)]
    att = [hex(stats[1]//256), hex(stats[1]%256)]
    defen = [hex(stats[2]//256), hex(stats[2]%256)]
    speed = [hex(stats[3]//256), hex(stats[3]%256)]
    spec_att = [hex(stats[4]//256), hex(stats[4]%256)]
    spec_def = [hex(stats[5]//256), hex(stats[5]%256)]
    
    # Gen 2 Structure (48): spc, item, mv1, mv2, mv3, mv4, OT (2), exp (3)
    # HP EV (2), Att EV (2), Def EV (2), Speed EV (2), Spec EV(2), IV (2),
    # mv1PP, mv2PP, mv3PP, mv4PP, friend, rus, caught (2), level, 
    # status, unused, curr HP (2), Max HP (2), att (2), def (2), speed (2),
    # spec att (2), spec def (2)        
    
    'Stats in hex and order'
    poke_hex = [species, item, mv1, mv2, mv3, mv4, OT[0], OT[1], exp[0],
                exp[1], exp[2], EV_HP[0], EV_HP[1], EV_att[0], EV_att[1], 
                EV_def[0], EV_def[1], EV_speed[0], EV_speed[1], EV_spec[0], 
                EV_spec[1], IV[0], IV[1], mv1PP, mv2PP, mv3PP, mv4PP, 
                friend, rus, caught[0], caught[1], level, status, unused,
                HP_curr[0], HP_curr[1], HP_max[0], HP_max[1], att[0], 
                att[1], defen[0], defen[1], speed[0], speed[1], 
                spec_att[0], spec_att[1], spec_def[0], spec_def[1]]
        
    poke_str = ""
    for i in range(0, len(poke_hex)):
        poke_str = poke_str + poke_hex[i] + comma 
    poke_str = poke_str + end
    
    party_hex.append(poke_str)
    
    'Nickname'
    nickname = text_hex(poke_name, gen)
    nickname_all.append(nickname)
    
    
    poke_line_hex = poke_line_hex + str(species) + comma
        
    'Intro Poke Line'
    for i in range(0, 7-1):         # Subtract number of pokemon
        poke_line_hex = poke_line_hex + '0xFF' + comma
    poke_line_hex = poke_line_hex + end
    
    'Trainer ID'
    trainerid = OT[0] + comma + OT[1] + comma + end
        
    return(party_hex, poke_line_hex, trainerid, nickname_all)