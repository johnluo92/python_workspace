'''Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elemnets, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Array with 1 element/empty array are monotonic.
'''

# o(n) time | o(1) space
def isMonotonic(a):
	increase = True
	length = len(a)
	i=0
	if length == 0:
		return 

	while i < length:
		if i == length-1:
			return True
		elif a[i]<=a[i+1]:
			i+=1
		else:
			increase = False
			i=0
			break

	while not increase and i < length:
		if i == length-1:
			return True
		elif a[i]>=a[i+1]:
			i+=1
		else:
			return False

array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

print(isMonotonic(array)) # True