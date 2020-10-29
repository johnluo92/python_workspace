'''Merge Sorted Arrays

Write a function that takes in a non-empty list of non-empty sorted arrays of integers and returns a merged list of all of those arrays.

The integers in the merged list should be in sorted order
'''

def mergeSortedArrays(arrays):
    # Write your code here.
	compareLow, ans = [], []
	empty = False
	while not empty:
		empty = True
		for row in range(len(arrays)):
			if len(arrays[row]):
				empty = False
				compareLow.append((row, arrays[row][0]))
		if not empty:
			low = min(compareLow, key= lambda x: x[1])
			row = low[0]
			# append smallest found num from the popped
			# value of the array where it was found			
			ans.append(arrays[row].pop(0))
			# reset comparison array
			compareLow = []
		print(ans)
	return ans

arrays = [[1, 5, 9, 21],
		[-1, 0],
		[-124, 81, 121],
		[3, 6, 12, 20, 150]]
		
print(mergeSortedArrays(arrays))