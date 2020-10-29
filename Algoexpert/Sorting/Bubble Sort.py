'''Bubble Sort

Implement bubble sort to sort an array'''

def bubbleSort(array):
    # Write your code here.
    length = len(array)
    rightIdx = length
    sort = False
    while rightIdx > 0:
        i = 0
        j = i + 1
        sort = False
        while j < length:
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                sort = True
            i += 1
            j += 1
        if sort is False:
            return array
        rightIdx -= 1
    return array

array = [8, 5, 2, 9, 5, 6, 3]

print(bubbleSort(array))