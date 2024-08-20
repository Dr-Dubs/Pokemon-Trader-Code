# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:33:29 2024

@author: jason
"""

# Code is reversible. It can encrypt or decrypt.

def gen3_encryption(PV1, PV2, TID, SID, data):        
    
    # Standard order of bytes (first to last)
    PV = format(PV1, '#018b')[2:] + format(PV2, '#018b')[2:]
    
    # Mod for sub-data order (AEGM), flipped order
    mod = int(format(PV2, '#018b')[2:] + format(PV1, '#018b')[2:], 2)%24
    
    # Standard order of bytes (first to last)
    TID_SID = format(int(TID, 16), '#018b')[2:] + format(int(SID, 16), '#018b')[2:]
    
    # XOR of PV and complete Trainer ID
    decrypt_key = int(PV, 2) ^ int(TID_SID, 2)
    
    decrypt_data = [0] * len(data)
    d_sum = 0
    for i in range(0, int(len(data)/2)):
        
        if type(data[0]) == str:
            byte1 = int(data[2*i], 16)
            byte2 = int(data[2*i+1], 16)
        elif type(data[0]) == int:
            byte1 = data[2*i]
            byte2 = data[2*i+1]
        
        bit32 = format(byte1, '#018b')[2:] + format(byte2, '#018b')[2:]        
        
        d_bit32 = format(int(bit32, 2) ^ decrypt_key, '#034b')[2:]     
        
        d_byte1 = hex(int(d_bit32[0:16], 2))
        d_byte2 = hex(int(d_bit32[16:32], 2))
        
        d_sum += int(d_byte1, 16)
        d_sum += int(d_byte2, 16)
        
        decrypt_data[2*i] = d_byte1
        decrypt_data[2*i+1] = d_byte2
        
    
    d_sum_hex = hex(d_sum)
    l = len(d_sum_hex)
    if l > 6:
        # Shrink to 16 bits
        d_sum_hex = d_sum_hex[0:2] + d_sum_hex[l-4:l]
        
    return(decrypt_data, mod, d_sum_hex)
        
        