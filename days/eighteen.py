import numpy, math
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

def run():
  input_data = [entry for entry in open('days/data/eighteen').read().splitlines()]
  print(puzzle_1(input_data))
  
def puzzle_1(input_data: list):
  points = extract_points(input_data)
  return calculate_area(points)

def shoelace_formula(points: list) -> int:
  max_index = len(points) - 1
  left_ladder = 0
  right_ladder = 0
  
  for counter in range(max_index+1):
    if counter + 1 <= max_index:
      end = counter + 1
    else:
      end = 0
    left_ladder = left_ladder + (points[counter][0]*points[end][1])
    right_ladder = right_ladder + (points[counter][1]*points[end][0])
  return 0.5 * abs(left_ladder-right_ladder)

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
  
  area = shoelace_formula(points)
  steps = sum_of_steps(points)
  inner_points = area - (steps/2) + 1

  return inner_points + steps

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