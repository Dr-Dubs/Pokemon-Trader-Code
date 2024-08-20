# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:05:48 2024

@author: jason
"""

def convert_gen2_to_gen3(gen2_data):
    
    # Gen 2 Structure (48, 8 bits each): spc, item, mv1, mv2, mv3, mv4, OT (2), 
    # exp (3), HP EV (2), Att EV (2), Def EV (2), Speed EV (2), Spec EV(2), 
    # IV (2), mv1PP, mv2PP, mv3PP, mv4PP, friend, rus, caught (2), level, 
    # status, unused, curr HP (2), Max HP (2), att (2), def (2), speed (2),
    # spec att (2), spec def (2)  
    
    'Gen 2 Import'
    species = gen2_data[0]
    item = gen2_data[1]
    mv1 = gen2_data[2]
    mv2 = gen2_data[3]
    mv3 = gen2_data[4]
    mv4 = gen2_data[5]
    OT_ID = gen2_data[6:8]
    exp = gen2_data[8:11]
    
    EV_HP       = gen2_data[11:13]
    EV_Att      = gen2_data[13:15]
    EV_Def      = gen2_data[15:17]
    EV_Speed    = gen2_data[17:19]
    EV_Spec     = gen2_data[19:21]
    
    IV = gen2_data[21:23]
    
    PP1 = gen2_data[23]
    PP2 = gen2_data[24]
    PP3 = gen2_data[25]
    PP4 = gen2_data[26]
    
    friend = gen2_data[27]
    rus = gen2_data[28]
    caught = gen2_data[29:31]
    level = gen2_data[31]
    status = gen2_data[32]
    unused = gen2_data[33]
    
    HP_curr     = gen2_data[34:36]
    HP_max      = gen2_data[36:38]
    Attack      = gen2_data[38:40]
    Defense     = gen2_data[40:42]
    Speed       = gen2_data[42:44]
    Sp_Attack   = gen2_data[44:46]
    Sp_Defense  = gen2_data[46:48]
    
    
    # Gen 3 Structure (100, little endian, 16 bits each): personality (4), 
    # OT ID (4), nickname (10), language (1), flags (1), OT name (7), 
    # markings (1), checksum (2), ???? (2), Data (48), status (4), level (1), 
    # mail ID (1), curr HP (2), Max HP (2), att (2), def (2), speed (2), 
    # spec att (2), spec def (2)
    
    # Stat difference because of nature
    
    'Stats in hex and order'
    gen3_data = []
    'PV'
    for i in range(0, len(PV_hex)):
        gen3_data.append(PV_hex[i])
        
    'OT number'
    for i in range(0, len(OT)):
        gen3_data.append(OT[i])
        
    'Poke nickname'    
    for i in range(0, len(nickname)):
        gen3_data.append(nickname[i])
        
    'Language and flags'    
    gen3_data.append(lang_flag)
    
    'OT name'
    for i in range(0, len(OT_name)):
        gen3_data.append(OT_name[i])
        
    'Checksum'
    gen3_data.append(checksum)
    
    'Unused'   
    gen3_data.append(unused)
    
    'Poke data'    
    for i in range(0, len(encrypted_data)):
        gen3_data.append(encrypted_data[i])
        
    'Status'    
    for i in range(0, len(status)):
        gen3_data.append(status[i])
        
    'Level and mail'    
    gen3_data.append(mail_level)
    
    'Stats'
    gen3_data.append(HP_curr)
    gen3_data.append(HP_max)
    gen3_data.append(att)
    gen3_data.append(defen)
    gen3_data.append(speed)
    gen3_data.append(spec_att)
    gen3_data.append(spec_def)
        
    
    return(gen3_data)