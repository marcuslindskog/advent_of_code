# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 07:33:15 2022

@author: ml1719
"""
import string

print('Day 3')

with open('day3_data.txt', 'r') as file:
    rucksacks = file.readlines()
    

letters = [char for char in string.ascii_lowercase+string.ascii_uppercase]
  
#Star 1  
items = []
score = 0
for rucksack in rucksacks:
    first_comp = set(rucksack[:int(len(rucksack)/2)])
    second_comp = set(rucksack[int(len(rucksack)/2):])
    score += letters.index(list(first_comp & second_comp)[0]) + 1
            
print(f'Star 1* \nThe score for all rucksacks where: {score}')
    
#Star 2
group_score = 0
for group in range(100):
    group_sack = rucksacks[3*group:3*group+3]
    elf1 = set(group_sack[0].replace('\n',''))
    elf2 = set(group_sack[1].replace('\n',''))
    elf3 = set(group_sack[2].replace('\n',''))
    group_score += letters.index(list(elf1 & elf2 & elf3)[0]) + 1
    
print(f'Star 2** \nThe score for all group rucksacks where: {group_score}')
