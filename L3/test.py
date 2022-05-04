import os
import math

# # Partition array into 2 sub-arrays
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


X = [3, 8, 2, 5, 1, 4, 7, 6]
print(Partition(X,0,7))
