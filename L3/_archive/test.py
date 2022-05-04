from array import array
import os
import math
from platform import architecture

with open('test.txt', 'r') as f:
    array = []
    input = f.read().splitlines()
    for x in input:
        array.append(int(x))

print(array)
# input = [12,2,45,5,32,6,5,4,3,2,1]