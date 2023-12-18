from days import one, two, three, four, five, six, seven, eight, nine, ten, eleven, thirteen, fourteen, fifteen, eighteen
import sys

def run(puzzle):
    puzzles = {
        "one": one.run,
        "two": two.run,
        "three": three.run,
        "four": four.run,
        "five": five.run,
        "six": six.run,
        "seven": seven.run,
        "eight": eight.run,
        "nine": nine.run,
        "ten": ten.run,
        "eleven": eleven.run,
        "thirteen": thirteen.run,
        "fourteen": fourteen.run,
        "fifteen": fifteen.run,
        "eighteen": eighteen.run,
    }
    puzzles[puzzle]()


run(sys.argv[1])
