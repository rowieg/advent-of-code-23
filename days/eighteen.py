import numpy, math

def run():
  input_data = [entry for entry in open('days/data/eighteen').read().splitlines()]
  print(puzzle_1(input_data))
  
def puzzle_1(input_data: list):
  points = extract_points(input_data)
  return calculate_area(points)

def calculate_area(points: list) -> int:
  max_index = len(points) - 1
  left_ladder = 0
  right_ladder = 0
  edges = len(points)
  steps = 0
  
  for counter in range(max_index+1):
    
    if counter + 1 <= max_index:
      end = counter + 1
    else:
      end = 0
    left_ladder = left_ladder + (points[counter][0]*points[end][1])
    right_ladder = right_ladder + (points[counter][1]*points[end][0])
    tmp_stp = math.sqrt((points[end][0]-points[counter][0])**2 + (points[end][1]-points[counter][1])**2)
    steps = steps + tmp_stp-1
  
  dirty_area = 0.5 * abs(left_ladder-right_ladder)
  
  edges_big = (edges/2) + 2
  edges_small = edges - edges_big
  area_edges = edges_big*0.75 + edges_small*0.25
  area_steps = steps/2
  
  
  return dirty_area + area_edges + area_steps

def extract_points(data: list) -> list:
  points = []
  position = (0,0)
  for entry in data:
    if entry[0] == "R":
      # modify +x 
      tmp = (position[0]+int(entry[2]), position[1])
    if entry[0] == "L":
      # modify -x
      tmp = (position[0]-int(entry[2]), position[1])
    if entry[0] == "D":
      # modify +y
      tmp = (position[0], position[1]+int(entry[2]))
    if entry[0] == "U":
      # modify -y
      tmp = (position[0], position[1]-int(entry[2]))
    position = tmp
    points.append(tmp)
  return points