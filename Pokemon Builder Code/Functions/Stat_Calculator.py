# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:21:30 2024

@author: jason
"""

from inter_calc import inter_calc
import math
import pandas as pd

def stat_calc(gen, level, base, DV, stat_exp, nature, IV, EV):
    
    l = len(base)
    stats = []
    if gen == 'Gen 1' or gen == 'Gen 2':
        
        for i in range(0, l):
            inter = inter_calc(base[i], DV[i], stat_exp[i], level, gen, 0, 0)
            if i == 0:
                HP = inter + level + 10
                stats.append(HP)
            else:
                stat = inter + 5
                stats.append(stat)
                
    else:
        
        
        data_fold = 'Data/Gen 3/'
        df_nature = pd.read_csv(data_fold + 'Nature_List.txt', 
                                 sep = '\t', header = 0,
                                 names = ['Mod', 'Nature', 'Inc', 'Dec'])
        
        for i in range(0, len(df_nature)):
            if df_nature.loc[i, 'Mod'] == nature:
                nature_inc = df_nature.loc[i, 'Inc']
                nature_dec = df_nature.loc[i, 'Dec']
                break
               
        nature_arr = [1, 1, 1, 1, 1]
        if nature_inc == 'Attack':
            nature_arr[0] = 1.1
        elif nature_inc == 'Defense':
            nature_arr[1] = 1.1
        elif nature_inc == 'Speed':
            nature_arr[2] = 1.1
        elif nature_inc == 'Sp. Attack':
            nature_arr[3] = 1.1
        else:
            nature_arr[4] = 1.1
            
        if nature_dec == 'Attack':
            nature_arr[0] = 0.9
        elif nature_dec == 'Defense':
            nature_arr[1] = 0.9
        elif nature_dec == 'Speed':
            nature_arr[2] = 0.9
        elif nature_dec == 'Sp. Attack':
            nature_arr[3] = 0.9
        else:
            nature_arr[4] = 0.9
        
        for i in range(0, l):
            inter = inter_calc(base[i], 0, 0, level, gen, IV[i], EV[i])
            if i == 0:
                HP = inter + level + 10
                stats.append(HP)
            else:
                stat = math.floor( (inter + 5)*nature_arr[i-1] )
                stats.append(stat)
        
    return(stats)