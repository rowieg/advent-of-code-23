import numpy as np
import math
from scipy import interpolate
from scipy.interpolate import RegularGridInterpolator

from math import comb
def puzzle_1(nums):
    n=len(nums)
    res=0
    for i,x in enumerate(nums):
        res+=x*comb(n,i)*(-1)**(n-1-i)
    return res

def puzzle_2(nums):
    n=len(nums)
    res=0
    for i,x in enumerate(nums):
        res+=x*comb(n,i+1)*(-1)**(i)
    return res

def run():
  numbers_list = [list(map(int, entry.split())) for entry in open('days/data/nine').read().splitlines()]
  counter_1 = 0
  counter_2 = 0
  for numbers in numbers_list:
    counter_1 = counter_1 + puzzle_1(numbers)
  for numbers in numbers_list:
    counter_2 = counter_2 + puzzle_2(numbers)

  return counter_1, counter_2
