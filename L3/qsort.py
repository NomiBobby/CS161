import os
import math


# Read input file into array
with open('QuickSort1.txt', 'r') as f:
    array = []
    input = f.read().splitlines()
    for x in input:
        array.append(int(x))

print("The original array is:", array)
print("------------------------------------")

# Partition Mode: # Mode 0, use first element, # Mode 1, use final element, # Mode 2 "median-of-three" pivot rule
mode = 0

# Define quick sort function
def qsort(X):
    
    # If array length is 1 return array
    X_len = len(X)
    if X_len <= 1:
        return X
    
    else:
        p_index = ChoosePivot(X, mode)
        
        # Preprocessing: swap pivot with the first element
        X[0], X[p_index] = X[p_index], X[0]
        
        # left boundary is the end of element 0 
        l = 0
        r = len(X) - 1
        p = X[l]
        # i is the left boundary
        i = l + 1
        for j in range(l + 1, r + 1):
            if X[j] < p:
                X[i], X[j] = X[j], X[i]
                i+=1
            # else do nothing
        # swap pivot to the middle
        X[l], X[i - 1] = X[i - 1], X[l]
        print("The partitioned array =", X)
        
        # Recursive call
        print("length of array = ", len(X), "i = ", i, "j = ", j)
        
        print(X[:i - 1])
        print(X[i:])
        X_sorted = qsort(X[:i - 1]) + [X[i-1]] + qsort(X[i:])
        return X_sorted
    
    
# Define ChoosePivot, return the index of the pivot
def ChoosePivot(X, mode):
    X_len = len(X)

    # Mode 0, use first element
    if mode == 0:
        return 0
    
    # Mode 1, use final element
    elif mode == 1:
        return X_len - 1

    # Mode 2, use median of first, middle and final element
    elif mode == 2:
        return MedianOfThree(X)
    
    
# Define "median-of-three" pivot rule, Returns the index of te median
def MedianOfThree(X):
    X_len = len(X) # >= 2
    a = X[0]
    if X_len % 2 == 0:
        b_index = X_len / 2 - 1
    else:
        b_index = [X_len - 1] / 2
    b = [b_index]
    c = X[-1]
    
    if a < b:
        if a > c:
            index = 0
        elif b < c:
            index = b_index
        else:
            index = X_len - 1
    else:# a>b
        if c > a:
            index = 0
        elif b > c:
            index = b_index
        else:
            index = X_len - 1
    return index


# Partition array into 2 sub-arrays
def Partition(X, l, r):
    # left boundary is the end of element 0 
    p = X[l]
    # i is the left boundary
    i = l + 1
    for j in range(l + 1, r + 1):
        if X[j] < p:
            X[i], X[j] = X[j], X[i]
            i+=1
        # else do nothing
    # swap pivot to the middle
    X[l], X[i - 1] = X[i - 1], X[l]
    return X

array_sorted = qsort(array)
print("The sorted array is: ", array_sorted)