import os

def read_input(file_path:str) -> list:
    with open(file_path, 'r') as file:
        data_input = file.readlines()
    return data_input
