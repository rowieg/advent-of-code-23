def run():
  data = open("days/data/fourteen", "r").read().splitlines()
  print("Run!")
  print(puzzle_1(data))
  
def puzzle_1(data):
  result = 0
  table_length = len(data)
  converted_rows = convert_to_rows(data)
  for row in converted_rows:
    stone_index = get_stone_positions(row)
    row_parts = row.split("#")
    rolling_stones = get_rolling_stones(row_parts)
    stone_sum = calculate_stone_sum(stone_index, rolling_stones, table_length)
    result = result + stone_sum
  return result

def puzzle_2(data):

  
  return 0

def convert_to_rows(table: list) -> list:
  converted_rows = []
  for x_row in range(0,len(table[0])):
    row = ""
    for y_row in table:
      row = row + str(y_row[x_row])
    converted_rows.append(row)
      
  return converted_rows
  
def get_stone_positions(row: str) -> list:
  return [index+1 for index, stone in enumerate(row) if stone == "#"]

def get_rolling_stones(parts: list[str]) -> list:
  return [part.count("O") for part in parts]

def calculate_stone_sum(stone_index: list, rolling_stones: list, table_length: int):
  if len(rolling_stones) < 1:
    return None
  
  part_1 = sum([(table_length-entry) for entry in range(0,rolling_stones[0])])
  
  part_2 = 0
    
  for e, stone in enumerate(stone_index):
    if e+1 < len(rolling_stones):
      partial_sum_list = []
      for entry in range(1,rolling_stones[e+1]+1):
        partial_sum_list.append(table_length-entry-stone+1)
      partial_sum = sum(partial_sum_list)
      part_2 = part_2 + partial_sum
  return part_1 + part_2