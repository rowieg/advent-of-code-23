from math import lcm
from itertools import cycle
from re import findall

def run(data_input):
    # print("Day eight puzzle a is:")
    # steps = puzzle_a(data_input[0], data_input[1])
    # print("Took {} steps".format(steps))

    print("Day eight puzzle b is:")
    #steps = puzzle_b(data_input[0], data_input[1])
    steps = puzzle_b_with_lcm(data_input[0], data_input[1])
    print("Took {} steps".format(steps))

def puzzle_a(input_string, input_list):
    converted_instructions = convert_instructions(input_string)
    converted_map = convert_map(input_list)
    steps = count_steps(converted_instructions, converted_map)
    return steps

def puzzle_b(input_string, input_list):
    converted_instructions = convert_instructions(input_string)
    converted_map = convert_map(input_list)
    steps = count_steps_as_ghost(converted_instructions, converted_map)
    return steps

def puzzle_b_with_lcm(input_string, input_list):
    converted_map = convert_map(input_list)
    steps = count_steps_with_lcm(input_string, converted_map)
    return steps


def puzzle_a(input_string, input_list):
    converted_instructions = convert_instructions(input_string)
    converted_map = convert_map(input_list)
    steps = count_steps_as_ghost(converted_instructions, converted_map)
    return steps

def convert_instructions(input_string: str) -> str:
    converted_string = input_string.replace("R", "1")
    converted_string = converted_string.replace("L", "0")
    return converted_string

def convert_map(list: list) -> dict:
    "AAA = (BBB, CCC)",
    converted_map = {}
    for entry in list:
        key = entry[0:3]
        tuple_string = entry[-9:-1]
        converted_map[key] = tuple(map(str, tuple_string.split(', ')))
    
    return converted_map

def count_steps(input_string, map_dict) -> int:
    position = "AAA"
    steps = 0
    while position != "ZZZ":
        for instruction in input_string:
            position = map_dict[position][int(instruction)]
            steps = steps + 1
            if position == "ZZZ":
                return steps
    return steps

def count_steps_as_ghost(input_string, map_dict) -> int:
    positions = []
    finish = False
    steps = 0
    for key in map_dict:
        if key.endswith("A"):
            positions.append(key)
    while finish != True:
        for instruction in input_string:
            steps = steps + 1
            for index, position in enumerate(positions):
                positions[index] = map_dict[position][int(instruction)]
            check = []
            for key in positions:
                check.append(key[-1])
            if set(check) == {"Z"}:
                finish = True
        print(steps)
        if steps > 100000000000:
            print("Broken! ", check, positions)
            return 1

    return steps    

def count_steps_with_lcm(input_string, map_dict):
    results = []
    for key in [i for i in map_dict.keys() if i.endswith("A")]:
        for i, command in enumerate(cycle(input_string.strip()), 1):
            key = map_dict[key][command == "R"]
            if key.endswith("Z"):
                results.append(i)
                break
    return lcm(*results)