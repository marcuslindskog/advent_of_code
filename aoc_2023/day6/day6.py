import os

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def solution_task_1():
    data_input = read_input('input.txt')

    times = [int(i) for i in data_input[0].split(':')[1].strip().split(' ') if i != '']
    distances = [int(i) for i in data_input[1].split(':')[1].strip().split(' ') if i != '']

    n_ways = []
    for time, distance in zip(times, distances):
        n_ways.append(len([i*(time-i) for i in range(0, time+1) if i*(time-i) > distance]))

    max_n_ways = 1
    for way in n_ways:
        max_n_ways *= way


    return max_n_ways

def solution_task_2():
    data_input = read_input('input.txt')

    time = int("".join([i for i in data_input[0].split(':')[1].strip().split(' ') if i != '']))
    distance = int("".join([i for i in data_input[1].split(':')[1].strip().split(' ') if i != '']))
    n_ways =len([i*(time-i) for i in range(0, time+1) if i*(time-i) > distance])

    return n_ways


if __name__ == '__main__':
    print(solution_task_1())
    print(solution_task_2())
