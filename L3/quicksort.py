from array import array
import os
import math
from platform import architecture

input = [12,2,45,5,32,6,5,4,3,2,1]

def quicksort(array):

    #print()
    #print("Sorting:", array)

    if len(array) <= 1:
        array_sorted = array
        return array_sorted

    else:
        # Define the index_pivot & split into left and right
        alpha = 0.5
        index_pivot = round(alpha * len(array))
        pivot = array[index_pivot]
        # #print("The pivot is:", pivot)

        left = []
        right = []
        for i in range(0,len(array)):
            if i != index_pivot:
                if array[i] <= pivot:
                    left.append(array[i])
                else:
                    right.append(array[i])
        #print(left, pivot, right)

        # Recuisive Call
        left_sorted = quicksort(left)
        right_sorted = quicksort(right)
        #print("Combining")

        # Combine left and right
        array_sorted = left_sorted + [pivot] + right_sorted
        #print("Sorted as: ", array_sorted)
        return array_sorted

print(input)
print(quicksort(input))