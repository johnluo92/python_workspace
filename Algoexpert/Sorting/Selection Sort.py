'''Selection Sort

Sort an array by implementing the algorithm selection sort.
'''

def selectionSort(array):
    # Write your code here.
    # input		[8, 5, 2, 9, 5, 6, 3] len = 7
	# expected	[2, 3, 5, 5, 6, 8, 9]
	length = len(array)
	for i in range(length-1):
		swapped = False
		min = array[i]
		for j in range(i+1,length):
			if array[j] < min:
				min = array[j]
				swapped = True
				swap = j
		if swapped:
			array[i], array[swap] = min, array[i]
	return array
                

array = [8, 5, 2, 9, 5, 6, 3]

print(selectionSort(array))