import os
import numpy as np

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def solution_task_1():
    data_input = read_input('input.txt')
    steps = data_input[0].strip()
    node_map = make_node_map(data_input)
    n_steps = find_number_of_steps('AAA',['ZZZ'], steps, node_map)

    return n_steps


def find_number_of_steps(start_node, end_nodes, steps, node_map):
    n_steps = 0
    current_node = start_node

    while True:
        step = n_steps % len(steps)
        direction = steps[step]
        current_node = get_next_node(node_map, current_node, direction)
        n_steps += 1
        if current_node in end_nodes:
            break

    return n_steps

def get_next_node(node_map,current_node, direction):
    if direction == 'R':
        next_node = node_map[current_node][1].strip()
    else:
        next_node = node_map[current_node][0].strip()

    return next_node

def make_node_map(data_input):
    nodes = {}
    for node in data_input[2:]:
        key = node.split("=")[0].strip()
        value = node.split("=")[1].strip().replace('(', '').replace(')', '').split(',')
        nodes.update({key:value})

    return nodes

def find_nodes(nodes, letter):
    found_nodes = []
    for key in nodes.keys():
        if key[-1] == letter:
            found_nodes.append(key)

    return found_nodes

def solution_task_2():
    data_input = read_input('input.txt')
    steps = data_input[0].strip()
    node_map = make_node_map(data_input)
    start_nodes = find_nodes(node_map, 'A')
    end_nodes = find_nodes(node_map, 'Z')

    cycles = []
    for start_node in start_nodes:
        cycle = find_number_of_steps(start_node,end_nodes, steps, node_map)
        cycles.append(cycle)

    n_steps = np.lcm.reduce(cycles)

    return n_steps


if __name__ == '__main__':
    print(solution_task_2())
