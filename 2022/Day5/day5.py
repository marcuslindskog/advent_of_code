# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 05:47:45 2022

@author: ml1719
"""
print('Day 5 \n')
with open('day5_data.txt', 'r') as file:
    data = file.readlines()

#Star 1
crates_star1 = [['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V'],
          ['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
          ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B'],
          ['R', 'S', 'C', 'L'],
          ['M', 'V', 'T', 'P', 'F', 'B'],
          ['T', 'R', 'Q', 'N', 'C'],
          ['G', 'V', 'R'],
          ['C', 'Z', 'S', 'P', 'D', 'L', 'R'],
          ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F'] ]

for move_order in data: 
    moves = move_order.split()
    n_moves = int(moves[1])
    from_bin = int(moves[3]) - 1
    to_bin  = int(moves[5]) - 1
    
    stop_move = 0
    while stop_move < n_moves:
        move_object = crates_star1[from_bin].pop()
        crates_star1[to_bin].append(move_object) 
        stop_move += 1

crate_order = ''.join([crate[-1] for crate in crates_star1])

print(f'Star 1* \nThe final crate order is {crate_order}.')

#SBPQRSCDF

#Star 2
crates_moved_2 = [['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V'],
          ['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
          ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B'],
          ['R', 'S', 'C', 'L'],
          ['M', 'V', 'T', 'P', 'F', 'B'],
          ['T', 'R', 'Q', 'N', 'C'],
          ['G', 'V', 'R'],
          ['C', 'Z', 'S', 'P', 'D', 'L', 'R'],
          ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F'] ]
  
for move_order in data: 
    moves = move_order.split()
    n_moves = int(moves[1])
    from_bin = int(moves[3]) - 1
    to_bin  = int(moves[5]) - 1
    
    move_object = crates_moved_2[from_bin][-n_moves:]
    del crates_moved_2[from_bin][-n_moves:]
    crates_moved_2[to_bin].extend(move_object) 
    #NB! list.append() to appen a single value. list.extend() to append
    #multiple values.

crate_order_2 = ''.join([crate[-1] for crate in crates_moved_2])

print(f'Star 2* \nThe final crate order is {crate_order_2}.')

#RGLVRCQSB