import os
import numpy as np

def solution_task_1():
    data_input = read_input('input.txt')
    data_matrix = data_to_matrix(data_input)

    history = 0
    for entry in data_matrix:
        all_diffs = find_diffs(entry)
        history += find_prediction(all_diffs)

    return history

def solution_task_2():
    data_input = read_input('input.txt')
    data_matrix = data_to_matrix(data_input)

    history = 0
    for entry in data_matrix:
        all_diffs = find_diffs(entry)
        history += find_postdiction(all_diffs)

    return history

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def find_postdiction(all_diffs):
    current_number_subs = 0
    for diff in all_diffs[::-1]:
        diff.insert(0, diff[0] - current_number_subs)
        current_number_subs = diff[0]

    postdiction = diff[0]

    return postdiction

def find_prediction(all_diffs):
    number_adds = []
    for diff in all_diffs[::-1]:
        number_adds.append(diff[-1])

    prediction = sum(number_adds[:-1]) + all_diffs[0][-1]

    return prediction

def find_diffs(entry):
    current_diff = entry
    all_diffs = [current_diff]
    while sum(current_diff) != 0:
        new_diff = list(np.diff(current_diff))
        current_diff = new_diff
        all_diffs.append(current_diff)

    return all_diffs

def data_to_matrix(data_input):
    data_output = []
    for row in data_input:
        data_output.append([int(i) for i in row.strip().split(' ')])

    return data_output



if __name__ == '__main__':
    print(solution_task_1())
    print(solution_task_2())

