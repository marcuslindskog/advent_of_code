import os

def read_input(file_name:str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data_input = file.readlines()

    return data_input

def solution_task_1():
    data_input = read_input('input.txt')

    seeds = []
    seed_to_soil = [[], []]
    soil_to_fertilizer = [[], []]
    fertilizer_to_water = [[], []]
    water_to_light = [[], []]
    light_to_temperature = [[], []]
    temperature_to_humidity = [[], []]
    humidity_to_location = [[], []]

    current_map = 0
    for row in data_input:
        row.strip()
        if 'seeds' in row:
            seeds = row.split(':')[1].strip().split(' ')
        elif 'seed-to-soil' in row:
            current_map = 1
            continue
        elif 'soil-to-fertilizer' in row:
            current_map = 2
            continue
        elif 'fertilizer-to-water' in row:
            current_map = 3
            continue
        elif 'water-to-light' in row:
            current_map = 4
            continue
        elif 'light-to-temperature' in row:
            current_map = 5
            continue
        elif 'temperature-to-humidity' in row:
            current_map = 6
            continue
        elif 'humidity-to-location' in row:
            current_map = 7
            continue

        if current_map > 0 and row != '\n':
            params = row.strip().split(' ')
            key = range(int(params[1]), int(params[1]) + int(params[2]))
            value = range(int(params[0]), int(params[0]) + int(params[2]))

        if current_map == 1:
            seed_to_soil[0].append(key)
            seed_to_soil[1].append(value)
        if current_map == 2:
            soil_to_fertilizer[0].append(key)
            soil_to_fertilizer[1].append(value)
        if current_map == 3:
            fertilizer_to_water[0].append(key)
            fertilizer_to_water[1].append(value)
        if current_map == 4:
            water_to_light[0].append(key)
            water_to_light[1].append(value)
        if current_map == 5:
            light_to_temperature[0].append(key)
            light_to_temperature[1].append(value)
        if current_map == 6:
            temperature_to_humidity[0].append(key)
            temperature_to_humidity[1].append(value)
        if current_map == 7:
            humidity_to_location[0].append(key)
            humidity_to_location[1].append(value)

    min_seed = None
    for seed_str in seeds:
        seed = int(seed_str)

        a, b, c = check_in_map(seed_to_soil, seed)
        if a:
            soil = seed_to_soil[1][b][c]
        else:
            soil = seed

        a, b, c = check_in_map(soil_to_fertilizer, soil)
        if a:
            fertilizer = soil_to_fertilizer[1][b][c]
        else:
            fertilizer = soil

        a, b, c = check_in_map(fertilizer_to_water, fertilizer)
        if a:
            water = fertilizer_to_water[1][b][c]
        else:
            water = fertilizer

        a, b, c = check_in_map(water_to_light, water)
        if a:
            light = water_to_light[1][b][c]
        else:
            light = water

        a, b, c = check_in_map(light_to_temperature, light)
        if a:
            temperature = light_to_temperature[1][b][c]
        else:
            temperature = light

        a, b, c = check_in_map(temperature_to_humidity, temperature)
        if a:
            humidity = temperature_to_humidity[1][b][c]
        else:
            humidity = temperature

        a, b, c = check_in_map(humidity_to_location, humidity)
        if a:
            location = humidity_to_location[1][b][c]
        else:
            location = humidity

        if min_seed is None:
            min_seed = location

        if min_seed > location:
            min_seed = location

    return min_seed

def check_in_map(map_to_check, item):
    for map_index, map_range in enumerate(map_to_check[0]):
        if item in map_range:
            return True, map_index, map_range.index(item)

    return False, None, None



if __name__ == '__main__':
    print(solution_task_1())
