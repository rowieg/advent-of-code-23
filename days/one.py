from utils import input

data_input = input.getInputData("one")

def run():
    print("Day one puzzle 1a is:")
    print(puzzle_a(data_input))

def puzzle_a(input):
    result = 0
    for line in input:
        line = convert_to_digit(line)
        print(line)
        all_number_string = "".join(c for c in line if c.isdigit())
        number_string = all_number_string[0] + all_number_string[-1]
        result = result + int(number_string)
    return result

def convert_to_digit(string):
    string = string.replace("one", "1")
    string = string.replace("two", "2")
    string = string.replace("three", "3")
    string = string.replace("four", "4")
    string = string.replace("five", "5")
    string = string.replace("six", "6")
    string = string.replace("seven", "7")
    string = string.replace("eight", "8")
    string = string.replace("nine", "9")
    return string