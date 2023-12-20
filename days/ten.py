debug_enabled = False

def debug(message, args = ""):
   if debug_enabled:
      print(message, args)
# from right to left
def from_right(current, next) -> bool:
   if current[1] == next[1] and current[0] > next[0]:
      debug("from right")
      return True
   return False

#from left to right
def from_left(current, next) -> bool:
   if current[1] == next[1] and current[0] < next[0]:
      debug("from right")
      return True
   return False

# from top to bottom
def from_top(current, next) -> bool:
   if current[0] == next[0] and current[1] < next[1]:
      debug("from top")
      return True
   return False

# from bottom to top
def from_bottom(current, next) -> bool:
   if current[0] == next[0] and current[1] > next[1]:
      debug("from bottom")
      return True
   return False


def find_start(current_position, next_position, steps, pipe_map):
      next_position_symbol = pipe_map[next_position[1]][next_position[0]]

      debug("Start here: ",pipe_map[current_position[1]][current_position[0]])
      debug("Next is here: ",next_position_symbol)

      if next_position_symbol == "." or next_position[0] < 0 or next_position[1] < 0:
         return False
      if next_position_symbol == "S":
          return True, steps + 1
      # is position is "L"
      if next_position_symbol == "L":
          if from_top(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0]+1,next_position[1]), steps, pipe_map)
          if from_right(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0],next_position[1]-1), steps, pipe_map)
      if next_position_symbol == "7":
          if from_left(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0],next_position[1]+1), steps, pipe_map)
          if from_bottom(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0]-1,next_position[1]), steps, pipe_map)
      if next_position_symbol == "J":
          if from_top(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0]-1,next_position[1]), steps, pipe_map)
          if from_left(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0],next_position[1]-1), steps, pipe_map)
          return False, steps
      if next_position_symbol == "F":
          if from_right(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0],next_position[1]+1), steps, pipe_map)
          if from_bottom(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0]+1,next_position[1]), steps, pipe_map)
      if next_position_symbol == "-":
          if from_right(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0]-1,next_position[1]), steps, pipe_map)
          if from_left(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0]+1,next_position[1]), steps, pipe_map)
      if next_position_symbol == "|":
          if from_top(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0],next_position[1]+1), steps, pipe_map)
          if from_bottom(current_position, next_position):
            steps = steps + 1
            return find_start(next_position, (next_position[0],next_position[1]-1), steps, pipe_map)

def puzzle_1(pipe_map):
    current_position = ()
    for index, entry in enumerate(pipe_map):
        if "S" in entry:
            current_position = (entry.index("S"), index)
    debug(pipe_map)
    position_up = (current_position[0], current_position[1] - 1)
    position_right = (current_position[0] + 1, current_position[1])
    position_down = (current_position[0], current_position[1] + 1)
    position_left = (current_position[0] - 1, current_position[1])

    results = []


    for next_position in [position_up, position_right, position_down, position_left]:
        debug("Start New Run")
        results.append(find_start(current_position, next_position, 0, pipe_map))
        
    return results


def puzzle_2():
    return 2


def run():
    pipe_map = [row for row in open("days/data/ten").read().splitlines()] 
    print(puzzle_1(pipe_map))

    return True
