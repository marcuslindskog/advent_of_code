# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 05:55:02 2022

@author: ml1719
"""

print('Day 6')

with open('day6_data.txt', 'r') as file:
    data = file.readlines()
    
string  = data[0]
#Star 1
start = 0
end = 4
not_found_yet = True
while not_found_yet:
    substring = string[start:end]
    if len(substring) == len(set(substring)):
        not_found_yet = False
    start += 1
    end += 1

print(f'Star 1* \Start marker is at: {end-1}')


#Star 2
start = 0
end = 14
not_found_yet = True
while not_found_yet:
    substring = string[start:end]
    if len(substring) == len(set(substring)):
        not_found_yet = False
    start += 1
    end += 1

print(f'Star 2* \nStart marker is at: {end-1}')
