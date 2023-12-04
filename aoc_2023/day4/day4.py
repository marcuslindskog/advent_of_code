import os
import re

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def solution_task_1():
    data_input = read_input('input.txt')

    values = []
    for card in data_input:
        split_w = card.split('|')[0].split(':')[1].strip().split(" ")
        winning_numbers = [int(i) for i in split_w if i.isdigit()]
        split_m = card.split('|')[1].strip().split(" ")
        my_numbers = [int(i) for i in split_m if i.isdigit()]
        n = 0
        card_value = 0
        for number in my_numbers:
            if number in winning_numbers:
                card_value = 2**n
                n += 1
        values.append(card_value)

    return sum(values)

def solution_task_2():
    data_input = read_input('input.txt')

    cards = {}
    for card in data_input:
        card_number = int("".join(re.findall(r'[\d+]', card.split(':')[0])))
        split_w = card.split('|')[0].split(':')[1].strip().split(" ")
        winning_numbers = [int(i) for i in split_w if i.isdigit()]
        split_m = card.split('|')[1].strip().split(" ")
        my_numbers = [int(i) for i in split_m if i.isdigit()]
        n_cards = 1
        cards[card_number] = {'wn': winning_numbers,
        'mn': my_numbers,
        'n':n_cards}

    for card_nr, card_prop in cards.items():
        n_winning = 0
        for number in card_prop['mn']:
            if number in card_prop['wn']:
                n_winning += 1
        if n_winning > 0:
            winning_array = list(range(card_nr+1,card_nr+n_winning+1))
        else:
            winning_array = []
        for card in winning_array:
            cards[card]['n'] += card_prop['n']

    sum_of_cards = 0
    for __, card_prop in cards.items():
        sum_of_cards += card_prop['n']

    return sum_of_cards


if __name__ == '__main__':
    print(solution_task_2())
