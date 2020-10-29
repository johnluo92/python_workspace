'''Permutations

Write a function that takes in an array of unique integers and returns an array of all permutations of those integers in no particular order.

If the input array is empty, the function should return an empty array.
'''


def getPermutations(array):
    # Write your code here.
	permutation_list = []
	permutationHelper(0, array, permutation_list)
	return permutation_list

def permutationHelper(i, array, permutation_list):
	if i == len(array) - 1:
		print(array[:])
		permutation_list.append(array[:])
	else:
		for j in range(i, len(array)):
			swap(i, j, array)
			permutationHelper(i+1, array, permutation_list)
			swap(i, j, array)
			
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

array = [1, 2, 3]
getPermutations(array) #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]