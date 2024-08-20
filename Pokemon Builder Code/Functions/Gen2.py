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

def gen2_converter(gen, party):
    
    party_hex = []
    nickname_all = []
    comma = ', '
    end = '\n'
    number_poke = hex(len(party))
    poke_line_hex = str(number_poke) + comma
    
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
    
    for poke in party:
        
        print(poke)
        
        'Base Stats'
        for i in range(0, len(df_stats)):
            if df_stats.loc[i, 'Name'] == poke[0]:
                base = [df_stats.loc[i, 'HP'], df_stats.loc[i, 'Att'], 
                        df_stats.loc[i, 'Def'], df_stats.loc[i, 'Speed'], 
                        df_stats.loc[i, 'Spec_Att'], df_stats.loc[i, 'Spec_Def']]
                
        'Species'
        for i in range(0, len(df_species)):
            if df_species.loc[i, 'Name'] == poke[0]:
                species = df_species.loc[i, 'DEC']
                species = hex(int(species))   
                
        'EV and IV'
        stat_exp = [0, 0, 0, 0, 0, 0]
        att_DV = random.randrange(16)
        def_DV = random.randrange(16)
        speed_DV = random.randrange(16)
        spec_DV = random.randrange(16)
        HP_DV = 8*(att_DV%2) + 4*(def_DV%2) + 2*(speed_DV%2) + spec_DV%2
        DV = [HP_DV, att_DV, def_DV, speed_DV, spec_DV, spec_DV] 
        DV1 = int('{0:04b}'.format(att_DV) + '{0:04b}'.format(def_DV), 2)
        DV2 = int('{0:04b}'.format(speed_DV) + '{0:04b}'.format(spec_DV), 2)
            
        'Stat Calculator'
        stats = stat_calc(gen, poke[1], base, DV, stat_exp, 0, 0, 0)
        
        'Moves'
        moves = [0, 0, 0, 0]
        moves_PP = [0, 0, 0, 0]
        for i in range(2, len(poke)):
            for j in range(0, len(df_moves)):
                if df_moves.loc[j, 'Name'] == poke[i]:
                    moves[i-2] = df_moves.loc[j, 'Dec']
                    moves_PP [i-2] = df_moves.loc[j, 'PP']
                    break
                
        'Exp'
        for i in range(0, len(df_exp)):
            if df_exp.loc[i, 'Name'] == poke[0]:
                exp_cat = df_exp.loc[i, 'Category']
                break
        
        'Stats'
        item = hex(0)
        mv1 = hex(moves[0])
        mv2 = hex(moves[1])
        mv3 = hex(moves[2])
        mv4 = hex(moves[3])
        OT = [hex(0), hex(0)]
        exp = exp_calc(gen, poke[1], exp_cat)
        EV_HP = [hex(0), hex(0)]
        EV_att = [hex(0), hex(0)]
        EV_def = [hex(0), hex(0)]
        EV_speed = [hex(0), hex(0)]
        EV_spec = [hex(0), hex(0)]
        IV = [hex(DV1), hex(DV2)]
        mv1PP = hex(moves_PP[0])
        mv2PP = hex(moves_PP[1])
        mv3PP = hex(moves_PP[2])
        mv4PP = hex(moves_PP[3])
        friend = hex(70)
        rus = hex(0)
        caught = [hex(0), hex(0)]
        level = hex(poke[1])
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
        nickname = text_hex(poke[0], gen)
        nickname_all.append(nickname)
        
        
        poke_line_hex = poke_line_hex + str(species) + comma
        
    'Intro Poke Line'
    for i in range(0, 7-len(party)):
        poke_line_hex = poke_line_hex + '0xFF' + comma
    poke_line_hex = poke_line_hex + end
    
    'Trainer ID'
    trainerid = OT[0] + comma + OT[1] + comma + end
        
    return(party_hex, poke_line_hex, trainerid, nickname_all)