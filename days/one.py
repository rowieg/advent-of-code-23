from utils import input

data_input = input.getInputData("one")

def run():
    print("Day one puzzle 1a is:")
    print(puzzle_a(data_input))

def puzzle_a(input):
    result = 0
    for line in input:
        line = replace_string_digits(line)
        print(line)
        all_number_string = "".join(c for c in line if c.isdigit())
        number_string = all_number_string[0] + all_number_string[-1]
        result = result + int(number_string)
    return result

def replace_string_digits(string):
    indexes = []
    indexes.append(string.find("one"))
    indexes.append(string.find("two"))
    indexes.append(string.find("three"))
    indexes.append(string.find("four"))
    indexes.append(string.find("five"))
    indexes.append(string.find("six"))
    indexes.append(string.find("seven"))
    indexes.append(string.find("eight"))
    indexes.append(string.find("nine"))

    for i in indexes:
        min_num = -1
        if i >= 0:
            min_num = i
    if min_num == -1: return string

    number_index = indexes.index(min_num)

    print(number_index)
    if number_index == 0:
        string = string.replace("one", "1")
    if number_index == 1:
        string = string.replace("two", "2")
    if number_index == 2:
        string = string.replace("three", "3")
    if number_index == 3:
        string = string.replace("four", "4")
    if number_index == 4:
        string = string.replace("five", "5")
    if number_index == 5:
        string = string.replace("six", "6")
    if number_index == 6:
        string = string.replace("seven", "7")
    if number_index == 7:
        string = string.replace("eight", "8")
    if number_index == 8:
        string = string.replace("nine", "9")


    return string

def convert_to_digit(string):
    one = string.find("one")
    two = string.find("two")
    three = string.find("three")
    four = string.find("four")
    five = string.find("five")
    six = string.find("six")
    seven = string.find("seven")
    eight = string.find("eight")
    nine = string.find("nine")

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