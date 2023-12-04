# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:33:30 2022

@author: ml1719
"""
print('Day 2')
rounds = []

with open('day2_data.txt', 'r') as file:
    data = file.readlines()

    for row in data:
        rounds.append(row.split())
#Star 1
responses = {'A': 'Rock',
             'B': 'Paper',
             'C': 'Scissors',
             'X': ['Rock', 1, 'Scissors'],
             'Y': ['Paper', 2, 'Rock'],
             'Z': ['Scissors', 3, 'Paper']}

score_star_1 = 0

for round in rounds:
    score_star_1 += responses[round[1]][1]
    if responses[round[0]] == responses[round[1]][0]:
        score_star_1 += 3
    elif responses[round[0]]  == responses[round[1]][2]:
        score_star_1 += 6
        

print(f'Star 1* \nTotal score with first scoring rule: {score_star_1}.')

#Star 2

elf_response = {'A': [2, 1, 3],
            'B': [3, 2, 1],
            'C': [1, 3, 2]}

score_star_2 = 0

for round in rounds:
    if round[1] == 'X':
        score_star_2 += (0 + elf_response[round[0]][2])
    elif round[1] == 'Y':
        score_star_2 += (3 + elf_response[round[0]][1]) 
    else:
        score_star_2 += (6 + elf_response[round[0]][0])  
        

print(f'Star 2** \nTotal score with second scoreing rule: {score_star_2}.')
