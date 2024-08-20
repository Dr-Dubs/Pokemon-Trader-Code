# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:59:36 2024

@author: jason
"""

import pandas as pd
from exp_calculator import exp_calc
import random
from byte8to16 import byte8to16
from gen3_encryption import gen3_encryption

def encoding(gen, poke, PV1, PV2, TID, SID):
    
    
    'Read in data'
    data_fold = 'Data/Gen 3/'
    
    df_species = pd.read_csv(data_fold + 'Pokemon_Species.txt', 
                             sep = '\t', header = 0,
                             names = ['HEX', 'DEC', 'MS', 'Name', 
                                       'Type 1', 'Type 2'])
        
    df_moves = pd.read_csv(data_fold + 'Move_List.txt', sep = '\t', 
                             header = 0, 
                             names = ['Dec', 'Name', 'Type', 'Category', 
                                      'PP', 'Power', 'Accuracy', 'Gen'])
    
    df_exp = pd.read_csv(data_fold + 'Exp_Categories.txt', sep = '\t', 
                             header = 0, 
                             names = ['Dec', 'Sprite', 'Name', 'Category'])
    
    df_friend = pd.read_csv(data_fold + 'Base_Friendship.txt', sep = '\t', 
                             header = 0, 
                             names = ['Dec', 'Sprite', 'Name', 'Base1', 'Base2'])
    
    df_order = pd.read_csv(data_fold + 'Sub_Data_List.txt', sep = '\t', 
                             header = 0, 
                             names = ['Mod', 'Order'])
    
    # Encryption: GAEM, all combinations
    
    # Data 1: Growth
    # species (2), item (2), exp (4), PP bonus (1), friend (1), unused (2)
    'Species (2 bytes)'
    for i in range(0, len(df_species)):
        if df_species.loc[i, 'Name'] == poke[0]:
            species_dec = int(df_species.loc[i, 'DEC'])
            species = hex(species_dec)
            
    'Exp Category'
    for i in range(0, len(df_exp)):
        if df_exp.loc[i, 'Name'] == poke[0]:
            exp_cat = df_exp.loc[i, 'Category']
            break
        
    'Friendship (1 byte, combined with PP Ups)'
    for i in range(0, len(df_friend)):
        if df_friend.loc[i, 'Name'] == poke[0]:
            friend = int(df_friend.loc[i, 'Base1'])
            friend = hex(friend) 
            break
    
    'Item (2 bytes)'
    item = hex(0)
    
    'Exp (4 bytes, small and then big)'
    level = poke[1]
    exp = exp_calc(gen, level, exp_cat)
    
    'PP bonus (1 byte) and friendship (1 byte)'
    PP_bonus = hex(0)
    PP_friend = byte8to16(friend, PP_bonus)
    
    'Unused (2 bytes)'
    unused = hex(0)
    
    G = [species, item, exp[0], exp[1], PP_friend, unused]
    
    
    # Data 2: Attacks moves (2 bytes), PP (1 byte)
    # mv1, mv2, mv3, mv4, mv1PP, mv2PP, mv3PP, mv4PP
    'Moves'
    moves = [0, 0, 0, 0]
    moves_PP = [0, 0, 0, 0]
    for i in range(2, len(poke)):
        for j in range(0, len(df_moves)):
            if df_moves.loc[j, 'Name'] == poke[i]:
                moves[i-2] = df_moves.loc[j, 'Dec']
                moves_PP[i-2] = df_moves.loc[j, 'PP']
            
    mv1 = hex(moves[0])
    mv2 = hex(moves[1])
    mv3 = hex(moves[2])
    mv4 = hex(moves[3])
    
    PP1 = hex(moves_PP[0])
    PP2 = hex(moves_PP[1])
    PP3 = hex(moves_PP[2])
    PP4 = hex(moves_PP[3]) 
    
    PP2_1 = byte8to16(PP2, PP1)
    PP4_3 = byte8to16(PP4, PP3)
    
    A = [mv1, mv2, mv3, mv4, PP2_1, PP4_3]
    
    # Data 3: EVs all 1
    # HP, Att, Def, Speed, Spec Att, Spec Def, Cool, Beauty, Cute, Smart, Tough, Feel
    'EVs'
    EV_dec = [0, 0, 0, 0, 0, 0]
    
    EV_HP = hex(EV_dec[0])
    EV_att = hex(EV_dec[1])
    EV_def = hex(EV_dec[2])
    EV_speed = hex(EV_dec[3])
    EV_spec_att = hex(EV_dec[4])
    EV_spec_def = hex(EV_dec[5])
    
    att_HP = byte8to16(EV_att, EV_HP)
    speed_def = byte8to16(EV_speed, EV_def)
    spec = byte8to16(EV_spec_def, EV_spec_att)
    
    'Contest'
    cool = hex(0)
    beauty = hex(0)
    cute = hex(0)
    smart = hex(0)
    tough = hex(0)
    feel = hex(0)
    
    beauty_cool = byte8to16(beauty, cool)
    smart_cute = byte8to16(smart, cute)
    tough_feel = byte8to16(tough, feel)
    
    E = [att_HP, speed_def, spec, beauty_cool, smart_cute, tough_feel]
    
    
    # Data 4: Misc.
    # rus (1), met loc (1), origin (2), IVs (4), ribbons (4)
    # IVs: single 32-bit value (Sp. Def., Sp. Att., Speed, Def, Att, HP)
    'Pokerus (1 byte)'
    rus = hex(0)
    
    'Met (1 byte, 254 = in-game trade)'
    met = hex(254)
    
    met_rus = byte8to16(met, rus)
    
    'Origins (2 bytes)'
    level_met = format(level, '#09b')[2:]       # 0 = hatch, otherwise actual level
    game_origin = format(3, '#06b')[2:]         # Sapphire(1), Ruby(2), Emerald(3), FireRed(4), LeafGreen(5), Colosseum or XD (15)
    poke_ball = format(4, '#06b')[2:]           # (1-12) Master, Ultra, Great, Poke, Safari, Net, Dive, Nest, Repeat, Timer, Luxury, Premier
    'Trainer Gender (0 = male, 1 = female)'
    OT_gender_bin = format(0, '#03b')[2:]
    origin_bin = OT_gender_bin + poke_ball + game_origin + level_met
    origin = hex(int(origin_bin, 2))
    
    'IVs (30 bits, 5 each, egg and ability as well to make 4 bytes)'
    IV_HP = random.randrange(32)
    IV_att = random.randrange(32)
    IV_def = random.randrange(32)
    IV_speed = random.randrange(32)
    IV_spec_att = random.randrange(32)
    IV_spec_def = random.randrange(32)
    IV_dec = [IV_HP, IV_att, IV_def, IV_speed, IV_spec_att, IV_spec_def]
    
    ability = PV1%2
    egg = 0
    
    IV_bin = bin(ability)[2:] + bin(egg)[2:]
    for i in range(len(IV_dec)-1, -1, -1):
        IV_bin += format(IV_dec[i], '#07b')[2:]
    
    IV_hex = [hex(int(IV_bin[16:32], 2)), hex(int(IV_bin[0:16], 2))]
        
    'Ribbons and Obedience (4 bytes)'
    ribbons = [hex(0), hex(0)]
    
    if species == '0x97' or species == '0x19A':
        # bit 31 = 1
        ribbons[1] = '0x8000'
    
    M = [met_rus, origin, IV_hex[0], IV_hex[1], ribbons[0], ribbons[1]]
    
    
    'Data Order'
    data_order = int(format(PV2, '#018b')[2:] + format(PV1, '#018b')[2:], 2)%24
    
    for i in range(0, len(df_order)):
        if df_order.loc[i, 'Mod'] == data_order:
            order_str = df_order.loc[i, 'Order']
            break
    
    data = []
    checksum = 0
    for i in order_str:
        if i == 'G':
            for j in range(0, len(G)):
                data.append(G[j])
                checksum += int(G[j], 16)
                
        elif i == 'A':
            for j in range(0, len(A)):
                data.append(A[j])
                checksum += int(A[j], 16)
                
        elif i == 'M':
            for j in range(0, len(M)):
                data.append(M[j])
                checksum += int(M[j], 16)
                
        else:
            for j in range(0, len(E)):
                data.append(E[j])
                checksum += int(E[j], 16)
                
                
    encrypt_data, mod, d_sum_hex = gen3_encryption(PV1, PV2, TID, SID, data)
            
    
    return(encrypt_data, IV_dec, EV_dec, checksum)
