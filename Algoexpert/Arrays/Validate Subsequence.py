'''Given two non-empty arrays of integers, write a function
that determines whether the second array is a subsequence of the
first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the number [1,3,4] form a subsequence of the array [1,2,3,4], and so do the numbers [2,4].'''

# o(n) time | o(1) space
def isValidSubsequence(array, sequence):
    # Write your code here.
	j = 0
	for i in array:
		if i == sequence[j]:
				j += 1
		if j == len(sequence):
			break
	return j == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(isValidSubsequence(array, sequence))