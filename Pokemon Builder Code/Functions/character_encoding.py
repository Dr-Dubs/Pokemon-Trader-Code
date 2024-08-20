# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:03:04 2024

@author: jason
"""

def text_hex(string, gen):
    
    if gen == 'Gen 1' or gen == 'Gen 2':
        hex_offset = int('0x80', 16)
        data_len = 11
        
        ord_offset = ord('a')
        offset = hex_offset - ord_offset
        comma = ', '
        end = '\n'
        
        upper = string[0]
        lower = str.lower(string[0])
        string = string.replace(upper, lower, 1)
        
        hex_str = ""
        for i in range(0, data_len):
            if i < len(string):
                hex_str = hex_str + (hex(ord(string[i]) + offset)) + comma
            else:
                hex_str = hex_str + hex(80) + comma
            
        hex_str = hex_str + end
        
        return(hex_str)
        
    
    elif gen =='Gen 3':
        
        upper = string[0]
        lower = str.lower(string[0])
        string = string.replace(upper, lower, 1)
        
        # Add 165 to end the string with 0xFF
        if len(string) % 2:
            string = string + chr(165)
        
        # Switch order for little endian
        little_str = ''.join([ string[x:x+2][::-1] for x in range(0, len(string), 2) ])
        
        # Gen 3 alphabet offset
        hex_offset = int('0xBB', 16)
        
        # Nickname is 10, Trainer name is 7
        data_len = 10
        
        ord_offset = ord('a')
        offset = hex_offset - ord_offset
        
        hex_str = []
        for i in range(0, data_len):
            if i < len(little_str):
                hex_str.append(hex(ord(little_str[i]) + offset))
            else:
                hex_str.append(hex(255))
                
        str_16bit = [0] * int(len(hex_str)/2)
        for i in range(0, int(len(hex_str)/2)):
            str_16bit[i] = hex_str[2*i] + hex_str[2*i+1][2:4]
            
        
        return(str_16bit)