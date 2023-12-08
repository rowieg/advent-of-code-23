import copy
import json
from functools import reduce

def solve_puzzle_a():

    seeds, *mappings = open('days/data/five').read().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))

    def lookup(inputs, mapping):
        for start, length in inputs:
            while length > 0:
                for m in mapping.split('\n')[1:]:
                    dst, src, len = map(int, m.split())
                    delta = start - src
                    if delta in range(len):
                        len = min(len - delta, length)
                        yield (dst + delta, len)
                        start += len
                        length -= len
                        break
                else: yield (start, length); break

    print(*[min(reduce(lookup, mappings, s))[0] for s in [
        zip(seeds, [1] * len(seeds)),
        zip(seeds[0::2], seeds[1::2])]])



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
    solve_puzzle_a()

    print("Day 5 result 2 is:")
    
