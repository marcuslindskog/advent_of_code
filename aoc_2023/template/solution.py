import os

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def solution_task_1():
    data_input = read_input('input.txt')

    return data_input

def solution_task_2():
    pass


if __name__ == '__main__':
    print(solution_task_1())
