# Import data from txt into the array
array = []
with open('IntegerArray.txt') as f:
# with open('sixarray.txt') as f:
# with open('example1.txt') as f:
    for line in f:
        array.append(int(line))
f.close()

def merge_sort(a):

    if(len(a) == 1):
        return [a, [0]]
    else:
        # location of the devide
        indice = len(a)//2
        a_l = a[0:indice]
        a_r = a[indice:]

        # Recursion call
        result_left = merge_sort(a_l)
        a_l_sorted = result_left[0]
        a_l_inversion = result_left[1][0]

        result_right = merge_sort(a_r)
        a_r_sorted = result_right[0]
        a_r_inversion = result_right[1][0]

        # Merge left and right
        i = 0
        j = 0
        a_sorted = []
        inversion_count = a_l_inversion + a_r_inversion
        for k in range(len(a)):
            if i < len(a_l_sorted) and j < len(a_r_sorted):
                if(a_l_sorted[i] <= a_r_sorted[j]):
                    a_sorted.append(a_l_sorted[i])
                    i+=1
                else:
                    # This is an inversion
                    a_sorted.append(a_r_sorted[j])
                    # Number of numbers left in left are all inversions
                    inversion_count = inversion_count + len(a_l_sorted) - i
                    # print("inversion count a = ", inversion_count)
                    j+=1
            elif i >= len(a_l_sorted):
                # no inversion left
                a_sorted.append(a_r_sorted[j])
                j+=1
            elif j >= len(a_r_sorted):
                a_sorted.append(a_l_sorted[i])
                i+=1
        return [a_sorted, [inversion_count]]

print(merge_sort(array)[1])