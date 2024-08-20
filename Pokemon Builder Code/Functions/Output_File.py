# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 07:11:39 2024

@author: jason
"""

'Read, edit, write output.h file for arduino to read'

def file_editing(gen, party_hex, poke_line_hex, trainerid, nickname_all):
    
    l = len(party_hex)
    
    if gen == 'Gen 1':
        file_name = 'Data/Gen 1/output_gen1.h'
        
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found")
            # return None
        
        old_line = lines[9]
        
        old_party = []
        for i in range(0, l): 
            old_party.append(lines[12+i])
            
        old_nickname = []
        for i in range(0, l): 
            old_nickname.append(lines[26+i])

        try:
            with open(file_name, 'w') as file:
                
                for line_number, line in enumerate(lines, 0):
                    
                    if line_number == 9:
                        modified_line = line.replace(old_line, poke_line_hex)
                        file.write(modified_line)
                        
                    elif 12 <= line_number < 12+l:
                        modified_line = line.replace(old_party[line_number-12], 
                                                     party_hex[line_number-12])
                        file.write(modified_line)
                            
                    elif 26 <= line_number < 26+l:
                        modified_line = line.replace(old_nickname[line_number-26], 
                                                     nickname_all[line_number-26])
                        file.write(modified_line)
                        
                    else:
                        file.write(line)
                print(f"File '{file_name}' has been successfully updated")
        except IOError:
            print(f"Error: Unable to write to file '{file_name}'")
        
        
    elif gen == "Gen 2":
        file_name = 'Data/Gen 2/output_gen2.h'
    
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found")
            # return None
        
        old_party = []
        for i in range(0, l): 
            old_party.append(lines[12+i])
            
        old_line = lines[8]
        old_trainer = lines[9]
        
        old_nickname = []
        for i in range(0, l): 
            old_nickname.append(lines[26+i])
    
        try:
            with open(file_name, 'w') as file:

                for line_number, line in enumerate(lines, 0):
                    
                    if line_number == 8:
                        modified_line = line.replace(old_line, poke_line_hex)
                        file.write(modified_line)
                        
                    elif line_number == 9:
                        modified_line = line.replace(old_trainer, trainerid)
                        file.write(modified_line)
                        
                    elif 12 <= line_number < 12+l:
                        modified_line = line.replace(old_party[line_number-12], 
                                                     party_hex[line_number-12])
                        file.write(modified_line)
                        
                    elif 26 <= line_number < 26+l:
                        modified_line = line.replace(old_nickname[line_number-26], 
                                                     nickname_all[line_number-26])
                        file.write(modified_line)
                      
                    else:
                        file.write(line)
                print(f"File '{file_name}' has been successfully updated")
        except IOError:
            print(f"Error: Unable to write to file '{file_name}'")