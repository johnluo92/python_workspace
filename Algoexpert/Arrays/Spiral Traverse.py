'''Spiral Traverse

Write a function that takes in an n x m two-dimensonal array (that can be square-shaped when n== m) and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral patterna all the way until every element has been visited.
'''

# o(n) time | o(n) space
def spiralTraverse(array):
    # Write your code here.
    spiral_list = []
    
    leftbound, rightbound = 0, len(array[0])
    upperbound, lowerbound = 0, len(array)
    
    while leftbound < rightbound and upperbound < lowerbound:
        
        for col in range(leftbound, rightbound):
            spiral_list.append(array[leftbound][col])

        for row in range(upperbound+1, lowerbound):
            spiral_list.append(array[row][rightbound-1])

        if upperbound != lowerbound-1:
            for col in reversed(range(leftbound, rightbound-1)):
                spiral_list.append(array[lowerbound-1][col])

        if leftbound != rightbound-1:
            for row in reversed(range(upperbound+1, lowerbound-1)):
                spiral_list.append(array[row][leftbound])
            
        leftbound += 1
        rightbound -= 1
        upperbound += 1
        lowerbound -= 1
        print('bottom\n', leftbound, rightbound, upperbound, lowerbound)
    print(spiral_list)
    return spiral_list

array = [[1, 2, 3, 4],
		[12, 13, 14, 5],
		[11, 16, 15, 6],
		[10, 9, 8, 7]]

# ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(threeNumberSum(array,targetSum))