import os
import re

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def solution_task_1():
    data_input = read_input('input.txt')
    possible_games = []
    for game in data_input:
        game_number = int(game.split(':')[0].split(' ')[1])
        rounds = game.split(':')[1].split(';')
        possible = True
        for game_round in rounds:
            try:
                blue = int(re.findall('(\d+)(?=\s*blue)', game_round)[0])
            except:
                blue = 0
            try:
                red = int(re.findall('(\d+)(?=\s*red)', game_round)[0])
            except:
                red = 0
            try:
                green = int(re.findall('(\d+)(?=\s*green)', game_round)[0])
            except:
                green = 0

            if red > 12 or green > 13 or blue > 14:
                possible = False

        if possible:
            possible_games.append(game_number)
    return sum(possible_games)


def solution_task_2():
    data_input = read_input('input.txt')
    cube_powers = []
    for game in data_input:
        game_number = int(game.split(':')[0].split(' ')[1])
        rounds = game.split(':')[1].split(';')
        possible = True
        blue_min = 0
        red_min = 0
        green_min = 0
        for game_round in rounds:
            try:
                blue = int(re.findall('(\d+)(?=\s*blue)', game_round)[0])
            except:
                blue = 0

            if blue > blue_min:
                blue_min = blue

            try:
                red = int(re.findall('(\d+)(?=\s*red)', game_round)[0])
            except:
                red = 0

            if red > red_min:
                red_min = red

            try:
                green = int(re.findall('(\d+)(?=\s*green)', game_round)[0])
            except:
                green = 0

            if green > green_min:
                green_min = green

        cube_powers.append(blue_min * red_min * green_min)

    return sum(cube_powers)


if __name__ == '__main__':
    print(solution_task_1())
    print(solution_task_2())
