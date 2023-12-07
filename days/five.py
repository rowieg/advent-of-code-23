import copy
import json

def convert_number(destination, source, step, seed):
    if source < seed and seed < (source + step):
        return ((seed - source) + destination, True)
    else:
        return (seed, False)

def convert_tuples(tuples, id):
    temp = id
    for index, tuple in enumerate(tuples):
        temp = convert_number(tuple[0],tuple[1],tuple[2], temp)
        if temp[1] == True:
            return temp[0]
        else:
            temp = temp[0]
    return temp

def run():
    print("Day 5 result 1 is:")
    
    print("result")

    print("Day 6 result 2 is:")
    
    print("result")