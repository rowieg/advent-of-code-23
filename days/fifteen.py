
def run():
  data = open("days/data/fifteen", "r").read().split(",")
  print(puzzle_1(data))
  
def puzzle_2(holiday_strings: list):
  boxes = {str(index): [] for index in range(0,256)}
  for holiday_string in holiday_strings:
    box_label, lens = arrange_lense(holiday_string)
    if lens[1] == None:
      for box in boxes:
        for lens_in_box in box:
          if lens_in_box[0] == lens[0]:
            index = box.index(lens_in_box)
            del box[index]
            break
    else:
      for box in boxes:
        for lens_in_box in box:
          if lens_in_box[0] == lens[0]:
            index = box.index(lens_in_box)
            box[index] = lens
            break
      boxes[box_label].append(lens)
  print(boxes)
  return boxes

def arrange_lense(holiday_string: str):
  lens = 0
  label = ""
  if "=" in holiday_string:
    tmp = holiday_string.split("=")
    label = tmp[0]
    lens = int(tmp[1])
  if "-" in holiday_string:
    tmp = holiday_string.split("-")
    label = tmp[0]
    lens = None
  
  box = str(initnumber_by_string(label))
  return box, (label, lens)
  
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