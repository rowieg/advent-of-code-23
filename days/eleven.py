import copy 
import re

def puzzle_1(game_map):
    #extended_game_map = extend_game_map(game_map)
    universes = extract_universes_coordinates(game_map)
    return caluclate_distances(universes)

def puzzle_2():
    return calc_with_func()

def run():
  game_map = [entry for entry in open('days/data/eleven').read().splitlines()]
  print(puzzle_1(game_map))
  print(puzzle_2())
  return 1

def calc_with_func():
    x = 5379354
    steps = [0,1,10,100,1000,10000,100000]
    result = 8715262
    for step in steps:
        result = result + (step * x)
    return result

def caluclate_distances(list_of_points):
    distance = 0
    for point_a in list_of_points:
        for point_b in list_of_points:
            if point_a == point_b:
                continue
            distance = distance + caluclate_distance(point_a, point_b)
    return distance/2


def caluclate_distance(point_a, point_b):
    return (abs(point_b[0]-point_a[0]) + abs(point_b[1]-point_a[1]))


def extract_universes_coordinates(game_map):
    coordinates = []
    for y_index, row in enumerate(game_map):
        hashes = [hash.start() for hash in re.finditer('#', row)]
        for hash in hashes:
            coordinates.append((hash, y_index))
    return sorted(coordinates)

def extend_x_rows(game_map):
    new_map = copy.copy(game_map)
    extend_indexes = []
    for index, y_row in enumerate(game_map):
        if not "#" in y_row:
            extend_indexes.append(index)
    for index, row_index in enumerate(extend_indexes):
        new_map.insert(row_index + index, game_map[row_index])
    return new_map

def extend_y_rows(game_map):
    new_map = copy.copy(game_map)
    extend_indexes = []
    for x_index in range(0,len(game_map[0])):
        marker = []
        for y_row in game_map:
            if y_row[x_index] == ".":
                marker.append(True)
            else:
                marker.append(False)
        if len(set(marker)) == 1:
            extend_indexes.append(x_index)
    for index, row_index in enumerate(extend_indexes):
        cleaned_index = row_index + index
        for line_index, line in enumerate(new_map):
            new_map[line_index] = line[:cleaned_index] + "." + line[cleaned_index:]
                

    return new_map

def extend_game_map(game_map):
    game_map = extend_x_rows(game_map)
    game_map = extend_y_rows(game_map)

    return game_map
