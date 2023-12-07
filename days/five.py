import copy
import json

def convert_number(destination, source, step, seed):
    if source < seed and seed < (source + step):
        return (seed - source) + destination
    else:
        return seed

def convert_tuples(tuples, id):
    temp = id
    for index, tuple in enumerate(tuples):
        print("Run number: ", index)
        temp = convert_number(tuple[0],tuple[1],tuple[2], temp)
    return temp
class SeedMap:
    map: {}

    def __init__(self, max):
        map = dict((str(n),n) for n in range(max))
        print(len(map))
        # for number in range(0,max):
        #     map[str(number)] = number
        self.set_map(map)

    def set_map(self, map):
        self.map = map

    def get_map(self):
        return self.map

    def create_map(self, source, destination, length):
        copy_map = copy.deepcopy(self.map)
        for add in range(0,length):
            copy_map[str(destination+add)] = source+add

        self.set_map(copy_map)
        
    def print(self):
        print(json.dumps(self.map, indent=8))

    def convert(self, number):
        return self.map[str(number)]

def run():
    print("Day 5 result 1 is:")
    
    print("result")

    print("Day 6 result 2 is:")
    
    print("result")