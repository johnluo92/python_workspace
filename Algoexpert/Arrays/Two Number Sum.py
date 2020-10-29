'''return the pair of numers in a given array
that sums up to the target number given as another input.
Return an empty array if no pairs sum up to the target.'''

# o(n) time | o(n) space
def twoNumberSum(array, targetSum):
    # Write your code here.
	
	dic = {i:targetSum-i for i in array}
	print(dic)
	
	for num in array:
		if not targetSum-num == num:
			if targetSum-num in dic:
				return [num, dic[num]]
	return []


arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

print(twoNumberSum(arr, target))