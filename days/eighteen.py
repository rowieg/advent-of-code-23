import re



def run():
  input_data = [entry for entry in open('days/data/eighteen').read().splitlines()]
  print(puzzle_1(input_data))
  print(puzzle_2(input_data))
  
def puzzle_1(input_data: list):
  points = extract_points(input_data)
  return calculate_area(points)

def puzzle_2(input_data: list):
  points = extraxt_part_2_points(input_data)
  return calculate_area(points)

def shoelace_formula(points: list) -> int:
  shoelace = 0
  
  for i in range(len(points) - 1):
    shoelace += points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1]
  
  return abs(shoelace) // 2

def sum_of_steps(points: list) -> int:
  
  max_index = len(points) - 1
  steps = 0
  
  for counter in range(max_index+1):
    if counter + 1 <= max_index:
      end = counter + 1
    else:
      end = 0
      
    steps = steps + abs((points[end][0]-points[counter][0]) + (points[end][1]-points[counter][1]))
    
  return steps
    

def calculate_area(points: list) -> int:
  
  perimeter = sum_of_steps(points)
  area = shoelace_formula(points) + perimeter// 2 + 1
  return area

def extract_points(data: list) -> list:
  points = [(0,0), (0,0)]
  position = (0,0)
  for entry_string in data:
    entry = entry_string.split()
    if entry[0] == "R":
      # modify +x 
      tmp = (position[0]+int(entry[1]), position[1])
    if entry[0] == "L":
      # modify -x
      tmp = (position[0]-int(entry[1]), position[1])
    if entry[0] == "D":
      # modify +y
      tmp = (position[0], position[1]-int(entry[1]))
    if entry[0] == "U":
      # modify -y
      tmp = (position[0], position[1]+int(entry[1]))
    position = tmp
    points.append(tmp)
    
  return points

def extraxt_part_2_points(data: list) -> list:
    points = [(0,0), (0,0)]
    position = (0,0)
    for entry_string in data:
      entry = entry_string.split()
      dirty_entry = entry[2]
      code = dirty_entry[2:-1]
      if code[-1] == "0":
        # modify +x 
        tmp = (position[0]+int(code[:-1],16), position[1])
      if code[-1] == "2":
        # modify -x
        tmp = (position[0]-int(code[:-1],16), position[1])
      if code[-1] == "1":
        # modify +y
        tmp = (position[0], position[1]-int(code[:-1],16))
      if code[-1] == "3":
        # modify -y
        tmp = (position[0], position[1]+int(code[:-1],16))
      position = tmp
      points.append(tmp) 
    return points