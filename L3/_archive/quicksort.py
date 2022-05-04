from array import array
import os
import math
from platform import architecture
from typing import final

with open('QuickSort.txt', 'r') as f:
    array = []
    input = f.read().splitlines()
    for x in input:
        array.append(int(x))

# Define the quicksort function
def quicksort(array):
    
    # Already Sorted
    if len(array) <= 1:
        array_sorted = array
        count = 0
        return [array_sorted, count]

    else:
        # Number of comparisons
        count = len(array) - 1

        # Define the index_pivot & split into left and right
        # alpha = 0.5
        # index_pivot = round(alpha * len(array))
        # pivot = array[index_pivot]

        # # use the first element as the pivot
        # index_pivot = 0
        # pivot = array[index_pivot]

        # # use the final element as the pivot
        # index_pivot = len(array) - 1
        # pivot = array[index_pivot]  

        # Using three median rule        
        first = array[0]
        if len(array) % 2 == 0:
            middle = array[len(array) // 2 - 1]
        else:
            middle = array[len(array) // 2]
        last = array[-1] 

        if first > middle:
            if first < final:
                median = first
            elif middle > final:
                median = middle
            else:
                median = final
        else:
            if first > final:
                median = first
            elif middle < final:
                median = middle
            else:
                median = final
        


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
        [left_sorted, count_l] = quicksort(left)
        [right_sorted, count_r] = quicksort(right)
        #print("Combining")

        # Combine left and right
        array_sorted = left_sorted + [pivot] + right_sorted
        count = count + count_l + count_r
        #print("Sorted as: ", array_sorted)
        return [array_sorted, count]

[sorted, count] = quicksort(array)

print("The number of comparisons is:", count)