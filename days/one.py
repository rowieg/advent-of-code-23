def run(data_input):
    print("Day one puzzle 1a is:")
    print(puzzle_a(data_input))

def puzzle_a(input):
    result = 0
    for line in input:
        modified_line = replace_digits(line)
        all_number_string = "".join(c for c in modified_line if c.isdigit())
        number_string = all_number_string[0] + all_number_string[-1]
        result = result + int(number_string)
    return result

def replace_digits(string):
    string = string.replace("one", "on1e")
    string = string.replace("two", "tw2o")
    string = string.replace("three", "thr3ee")
    string = string.replace("four", "fo4ur")
    string = string.replace("five", "fi5ve")
    string = string.replace("six", "si6x")
    string = string.replace("seven", "se7ven")
    string = string.replace("eight", "eig8th")
    string = string.replace("nine", "ni9ne")
    return string