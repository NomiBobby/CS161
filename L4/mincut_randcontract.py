import numpy as np

with open('kragerMinCut.txt') as f:
    lines = f.readlines()
f.close()

# Read file into adjList as as List, values as int
adjList = []

for row in lines:
    row_delimited = row.split("\t")[:-1]
    row_delimited_int = []
    for x in row_delimited:
        row_delimited_int.append(int(x))
    adjList.append(row_delimited_int)

print(adjList)


