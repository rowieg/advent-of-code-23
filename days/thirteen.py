import numpy, copy

def flip_matrix(matrix):
  rotated_matrix = numpy.rot90(matrix)
  fliped_matrix = numpy.flipud(rotated_matrix)
  return fliped_matrix.tolist()

def extract_game_maps(list):
  new_list = []
  sub_list = []
  for row in list:
    if len(row) == 0:
      new_list.append(copy.deepcopy(sub_list))
      sub_list.clear()
      continue
    sub_list.append(row)
  new_list.append(copy.deepcopy(sub_list))
  return new_list

def convert_game_map(list):
  convert_game_map = []
  for row in list:
    new_row = row.replace("#","1")
    new_row = new_row.replace(".","0")
    convert_game_map.append([int(char) for char in new_row] )
  return convert_game_map

def find_mirror_line_index(list):
  mirror_line_index = []
  list_len=len(list)
  for e, row in enumerate(list):
    if e+1 < list_len:
      if row == list[e+1]:
        mirror_line_index.append(list.index(row))

  return mirror_line_index
    
def find_perfect_mirror(game_map, index_x, index_y) -> tuple():
  horizontal_matches=[0]
  vertical_matches=[0]
  #print(index_x, index_y)
  for x in index_x:
    horizontal_match = 0
    if x != None:
      for counter in range(int(len(game_map))):
        in_lower_boundary = int(x-counter) >= 0
        in_upper_boundary = int(x+counter+1) < len(game_map)
        if in_lower_boundary and in_upper_boundary:
          if game_map[x-counter] == game_map[x+counter+1]:
            horizontal_match = horizontal_match + 1
          elif horizontal_match != 0:
            horizontal_matches.append(horizontal_match)
            break
      horizontal_matches.append(horizontal_match)

  for y in index_y:
    vertical_match = 0
    if y != None:  
      fliped_map = flip_matrix(game_map)
      for counter in range(int(len(fliped_map))):
        in_lower_boundary = int(y-counter) >= 0
        in_upper_boundary = int(y+counter+1) < len(fliped_map)
        if in_lower_boundary and in_upper_boundary:
          if fliped_map[y-counter] == fliped_map[y+counter+1]:
            vertical_match = vertical_match + 1
          elif vertical_match != 0:
            vertical_matches.append(vertical_match)
            break
      vertical_matches.append(vertical_match)

  #print(vertical_matches)
  if max(vertical_matches) > max(horizontal_matches):
    #print("Check this: ",index_y, vertical_matches)
    index = vertical_matches.index(max(vertical_matches)) - 1
    return ("Vertical", index_y[index]+1)
  if max(horizontal_matches) > max(vertical_matches):
    index = horizontal_matches.index(max(horizontal_matches)) - 1
    return ("Horizontal", index_x[index]+1)
  return ("None", None)

def puzzle_1(test_data):
  game_maps = extract_game_maps(test_data)
  converted_game_maps = []
  sum = 0


  for map in game_maps:
      converted_game_map = convert_game_map(map)
      converted_game_maps.append(converted_game_map)

  for e, game_map in enumerate(converted_game_maps):
        index_x = find_mirror_line_index(game_map)
        index_y = find_mirror_line_index(flip_matrix(game_map))
        result = find_perfect_mirror(game_map, index_x, index_y)
        #print("Result: ", result)
        if result[0] == "Vertical":
          sum = sum + result[1]
        elif result[0] == "Horizontal":
          sum = sum + result[1]*100

  return sum

def run():
  input = open("days/data/thirteen", "r") .read().splitlines()
  print(puzzle_1(input))