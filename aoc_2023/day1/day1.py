import os
import re

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def solution_task_1():
    data_input = read_input('input.txt')
    entries = []
    for line in data_input:
        numbers = re.findall('([0-9]+)', line)
        number = "".join(numbers)
        entries.append(int(number[0] +number[-1]))

    return sum(entries)

def solution_task_2():
    data_input = read_input('input.txt')
    number_lookup = {'one':'1',
                     'two':'2',
                     'three':'3',
                     'four':'4',
                     'five':'5',
                     'six': '6',
                     'seven':'7',
                     'eight':'8',
                     'nine':'9'}
    entries = []
    for line in data_input:
        numbers = re.findall('([0-9]+|one|two|three|four|five|six|seven|eight|nine)', line)
        data_number_entries = []
        for number in numbers:
            if number in number_lookup:
                data_number_entries.append(number_lookup[number])
            else:
                data_number_entries.append(number)
        number = "".join(data_number_entries)
        entries.append(int(number[0] +number[-1]))

    return sum(entries)


if __name__ == '__main__':
    print(solution_task_1())
    print(solution_task_2())
