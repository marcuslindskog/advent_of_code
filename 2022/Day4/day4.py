# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:28:48 2022

@author: ml1719
"""

print('Day 4 \n')

with open('day4_data.txt', 'r') as file:
    data = file.readlines()
    
#Star 1
full_coverage = 0
for pair in data:
    first_elf = set(range(int(pair.split(',')[0].split('-')[0]), int(pair.split(',')[0].split('-')[1]) +1))
    second_elf = set(range(int(pair.split(',')[1].split('-')[0]), int(pair.split(',')[1].split('-')[1]) +1))

    if len(first_elf & second_elf) == len(first_elf) or len(first_elf & second_elf) == len(second_elf):
        full_coverage += 1
        
print(f'Star 1* \nThere is full coverage in {full_coverage} pairs. \n')

#Star 2
partial_coverage = 0
for pair in data:
    first_elf = set(range(int(pair.split(',')[0].split('-')[0]), int(pair.split(',')[0].split('-')[1]) +1))
    second_elf = set(range(int(pair.split(',')[1].split('-')[0]), int(pair.split(',')[1].split('-')[1]) +1))

    if len(first_elf & second_elf) > 0:
        partial_coverage += 1
        
print(f'Star 2* \nThere is partial coverage in {partial_coverage} pairs.')

