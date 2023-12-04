import os
import re
from pathlib import Path

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def solution_task_1():
    data_input = read_input('input.txt')

    data_matrix = []
    for row in data_input:
        data_matrix.append(list(row.strip()))

    numbers = []
    number_places = []
    for i, row in enumerate(data_matrix):
        number = ''
        np =[]
        for j, entry in enumerate(row):
            if entry.isdigit():
                number += entry
                np.append([i, j])
                if j == len(row) - 1 and number != '':
                     numbers.append(int(number))
                     number_places.append(np)
            else:
                if number != '':
                    numbers.append(int(number))
                    number_places.append(np)
                    number = ''
                    np = []

    parts = []
    non_parts = []

    for number, number_places in zip(numbers, number_places):
        row_above = max(number_places[0][0] - 1, 0)
        row_below = min(number_places[0][0] + 2, len(data_matrix))
        column_before = max(number_places[0][1] - 1, 0)
        column_after = min(number_places[-1][1] + 2, len(data_matrix[0]))
        non_part = True
        for row in data_matrix[row_above:row_below]:
            chars = re.findall(r'[^\d.]', ''.join(row[column_before:column_after]))

            if len(chars) > 0:
                parts.append(number)
                non_part = False
                continue

    return sum(parts)


def solution_task_2():
    data_input = read_input('input.txt')

    data_matrix = []
    for row in data_input:
        data_matrix.append(list(row.strip()))

    numbers = []
    number_places = []
    gear_places = []
    for i, row in enumerate(data_matrix):
        number = ''
        np =[]
        for j, entry in enumerate(row):
            if entry == '*':
                gear_places.append([i, j])

            if entry.isdigit():
                number += entry
                np.append([i, j])
                if j == len(row) - 1 and number != '':
                     numbers.append(int(number))
                     number_places.append(np)
            else:
                if number != '':
                    numbers.append(int(number))
                    number_places.append(np)
                    number = ''
                    np = []
    gear_parts = [[] for __ in range(len(gear_places))]
    for number, number_places in zip(numbers, number_places):
        row_above = max(number_places[0][0] - 1, 0)
        row_below = min(number_places[0][0] + 2, len(data_matrix))
        column_before = max(number_places[0][1] - 1, 0)
        column_after = min(number_places[-1][1] + 2, len(data_matrix[0]))
        non_part = True
        for row in data_matrix[row_above:row_below]:
            chars = re.findall(r'[*]', ''.join(row[column_before:column_after]))
            if len(chars) > 0:
                for i, gear_place in enumerate(gear_places):
                    in_row = gear_place[0] >= row_above and gear_place[0] < row_below
                    in_col = gear_place[1] >= column_before and gear_place[1] < column_after
                    if in_row and in_col:
                        gear_parts[i].append(number)
                        continue
    final_sum = 0
    for parts in gear_parts:
        if len(parts) == 2:
            final_sum += parts[0]*parts[1]


    return final_sum

if __name__ == '__main__':
    print(solution_task_1())
    print(solution_task_2())

