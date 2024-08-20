# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:19:16 2024

@author: jason
"""

import pandas as pd
from Stat_Calculator import stat_calc
from character_encoding import text_hex
from encoding import encoding
import random
from byte8to16 import byte8to16

def gen3_converter(gen, party):
    
    party_hex = []
    
    data_fold = 'Data/Gen 3/'
    
    df_stats = pd.read_csv(data_fold + 'Base_Stats.txt', sep = '\t', 
                             header = 0, 
                             names = ['Dex', 'Sprite', 'Name', 'HP', 
                                       'Att', 'Def', 'Spec_Att', 'Spec_Def', 
                                       'Speed', 'Total', 'Avg'])
    
    df_gender_ratio = pd.read_csv(data_fold + 'Gender_Ratio.txt', sep = '\t', 
                             header = 0, 
                             names = ['Name', 'GR'])
    
    for poke in party:
        
        print(poke)
        
        'Gender (1 byte, necessary fpr PV)'
        for i in range(0, len(df_gender_ratio)):
            if df_gender_ratio.loc[i, 'GR'] == 0:
                gender = 0
            elif df_gender_ratio.loc[i, 'GR'] == 1:
                gender = 254
            elif df_gender_ratio.loc[i, 'GR'] == '-':
                gender = 255
            else:
                gender = random.randrange(253) + 1
        
        'Personality Value (4 bytes)'
        PV0 = random.randrange(256)
        PV0_gen = byte8to16(hex(PV0), hex(gender))
        PV1 = int(PV0_gen, 16)
        PV2 = random.randrange(256*256)
        PV_hex = [hex(PV1), hex(PV2)]
        
        'Nature (0-24)'
        nature = int(format(PV2, '#018b')[2:] + format(PV1, '#018b')[2:], 2)%25
        
        'OT Trainer ID (4 bytes, Trainer ID, Secret ID)'
        TID = hex(0)
        SID = hex(0)
        OT = [TID, SID]
        
        'Nickname (10 bytes)'
        nickname = text_hex(poke[0], gen)
        
        'Language and Flag'
        lang = hex(2)       # English
        flag = hex(2)       # bit 1 = 1 
        
        if len(lang) == 4:
            lang_flag = flag + lang[2:4]
        else:
            lang_flag = flag + '0' + lang[2]
            
        'Trainer name (7 bytes), Markings (1 byte, 0x00)'
        OT_name = text_hex('Hacker', gen)[0:4]
        
        'Markings'
        mark = str(0)
        OT_name[3] = OT_name[3].replace('f', mark, 2)
        
        'Unused'
        unused = hex(0)
        
        'Data and Encryption'
        encrypted_data, IV, EV, checksum_int = encoding(gen, poke, PV1, PV2, 
                                                        TID, SID)
        checksum = hex(checksum_int % 65536)
        
        'Status'
        status = [hex(0), hex(0)]
        
        'Level (1 byte, combined with mail ID, 0xFF)'
        level = hex(poke[1])
        mail = hex(255)
        mail_level = byte8to16(mail, level)
        
        'Base Stats'
        for i in range(0, len(df_stats)):
            if df_stats.loc[i, 'Name'] == poke[0]:
                base = [df_stats.loc[i, 'HP'], df_stats.loc[i, 'Att'], 
                        df_stats.loc[i, 'Def'], df_stats.loc[i, 'Spec_Att'],
                        df_stats.loc[i, 'Spec_Def'], df_stats.loc[i, 'Speed']]
                break
        
        'Stat Calculator'
        stats = stat_calc(gen, poke[1], base, 0, 0, nature, IV, EV)
        
        HP_curr = hex(stats[0])
        HP_max = hex(stats[0])
        att = hex(stats[1])
        defen = hex(stats[2])
        speed = hex(stats[3])
        spec_att = hex(stats[4])
        spec_def = hex(stats[5])
        
        # Gen 3 Structure (100, little endian): personality (4), OT ID (4), nickname (10), 
        # language (1), flags (1), OT name (7), markings (1), checksum (2)
        # ???? (2), Data (48), status (4), level (1), mail ID (1), curr HP (2), 
        # Max HP (2), att (2), def (2), speed (2), spec att (2), spec def (2)
            
        'Stats in hex and order'
        poke_hex = []
        'PV'
        for i in range(0, len(PV_hex)):
            poke_hex.append(PV_hex[i])
            
        'OT number'
        for i in range(0, len(OT)):
            poke_hex.append(OT[i])
            
        'Poke nickname'    
        for i in range(0, len(nickname)):
            poke_hex.append(nickname[i])
            
        'Language and flags'    
        poke_hex.append(lang_flag)
        
        'OT name'
        for i in range(0, len(OT_name)):
            poke_hex.append(OT_name[i])
            
        'Checksum'
        poke_hex.append(checksum)
        
        'Unused'   
        poke_hex.append(unused)
        
        'Poke data'    
        for i in range(0, len(encrypted_data)):
            poke_hex.append(encrypted_data[i])
            
        'Status'    
        for i in range(0, len(status)):
            poke_hex.append(status[i])
            
        'Level and mail'    
        poke_hex.append(mail_level)
        
        'Stats'
        poke_hex.append(HP_curr)
        poke_hex.append(HP_max)
        poke_hex.append(att)
        poke_hex.append(defen)
        poke_hex.append(speed)
        poke_hex.append(spec_att)
        poke_hex.append(spec_def)
            
        print(poke_hex)
        
        party_hex.append(poke_hex)
        
        
    return(party_hex, 0, 0, 0)