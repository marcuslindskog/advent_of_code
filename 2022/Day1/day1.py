# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 06:10:09 2022

@author: ml1719
"""

print('Day 1')
#Star 1
all_e = []
current_e = []

with open('day1_data.txt', 'r') as file:
    data = file.readlines()
    for row in data:
        if row == '\n':
            all_e.append(sum(current_e))
            current_e = []
        else:
            current_e.append(int(row))

        
maximum_elf = max(all_e)
        
print(f'Star 1* \nThe elf with the most food has {maximum_elf} calories.')

#Star 2
all_e.sort(reverse = True)
top_3_elfs = sum(all_e[0:3])

print(f'Star 2* \nThe top three elfs have {top_3_elfs} calories in total.')
