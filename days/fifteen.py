
def run():
  data = open("days/data/fifteen", "r").read().split(",")
  print(puzzle_1(data))
  
def puzzle_1(holiday_strings: list):
  current_value = 0
  for holiday_string in holiday_strings:
    current_value = current_value + initnumber_by_string(holiday_string)
  return current_value

def initnumber_by_string(holiday_string: str):
  current_value = 0
  for char in holiday_string:
    current_value = holiday_ascii_algorithm(char, current_value)
  return current_value

def holiday_ascii_algorithm(char: str, current_value: int):
  current_value = current_value + ord(char)
  current_value = current_value * 17
  current_value = current_value % 256
  return current_value