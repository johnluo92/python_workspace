'''Insertion Sort

Sort an array by implementing insertion sort.
'''

def insertionSort(array):
    # Write your code here.
    length = len(array)
    inserted = False
    for i in range(1,length):
        while i>0 and array[i]<array[i-1]:
            array[i-1], array[i] = array[i], array[i-1]
            i -= 1
    return array
                

array = [8, 5, 2, 9, 5, 6, 3]

print(insertionSort(array))