import os

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def solution_task_1():
    data_input = read_input('input.txt')
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    hands_bids = []
    card_values = []
    for data in data_input:
        hand = data.split(' ')[0]
        bid = int(data.split(' ')[1])
        hands_bids.append([hand, bid])
        card_value = [cards.index(i) for i in hand]
        card_values.append(card_value)

    hand_types = []
    for hand in hands_bids:
        card_hand = hand[0]
        hand_type = None
        hand_count = []
        for card in cards:
            hand_count.append(card_hand.count(card))
        if max(hand_count) == 5:
            hand_type = 7
        elif max(hand_count) == 4:
            hand_type = 6
        elif 3 in hand_count and 2 in hand_count:
            hand_type = 5
        elif max(hand_count) == 3:
            hand_type = 4
        elif hand_count.count(2) == 2:
            hand_type = 3
        elif max(hand_count) == 2:
            hand_type = 2
        else:
            hand_type = 1

        hand_types.append(hand_type)

    all_hand_info = [(x, y, z[0], z[1], z[2], z[3], z[4]) for y, x, z in zip(hand_types, hands_bids, card_values)]

    sorted_hands = sorted(all_hand_info, key=lambda x: (x[1], x[2], x[3], x[4], x[5], x[6]))


    winnings = 0
    for rank, hand in enumerate(sorted_hands):
        winnings += hand[0][1]*(rank+1)

    return winnings

def solution_task_2():
    data_input = read_input('input.txt')
    cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    hands_bids = []
    card_values = []
    for data in data_input:
        hand = data.split(' ')[0]
        bid = int(data.split(' ')[1])
        hands_bids.append([hand, bid])
        card_value = [cards.index(i) for i in hand]
        card_values.append(card_value)

    hand_types = []
    for hand in hands_bids:
        card_hand = hand[0]
        hand_type = None
        hand_count = []
        for card in cards:
            hand_count.append(card_hand.count(card))
        joker_count = hand_count[0]
        if max(hand_count[1:]) + joker_count == 5:
            hand_type = 7
        elif max(hand_count[1:]) + joker_count ==4 :
            hand_type = 6
        elif (3 in hand_count[1:] and 2 in hand_count[1:]) or (hand_count[1:].count(2) == 2 and joker_count == 1):
            hand_type = 5
        elif max(hand_count[1:]) + joker_count == 3:
            hand_type = 4
        elif hand_count[1:].count(2) == 2 or joker_count == 2:
            hand_type = 3
        elif max(hand_count[1:]) + joker_count == 2:
            hand_type = 2
        else:
            hand_type = 1

        hand_types.append(hand_type)

    all_hand_info = [(x, y, z[0], z[1], z[2], z[3], z[4]) for y, x, z in zip(hand_types, hands_bids, card_values)]

    sorted_hands = sorted(all_hand_info, key=lambda x: (x[1], x[2], x[3], x[4], x[5], x[6]))


    winnings = 0
    for rank, hand in enumerate(sorted_hands):
        winnings += hand[0][1]*(rank+1)

    return winnings


if __name__ == '__main__':
    print(solution_task_1())
    print(solution_task_2())
