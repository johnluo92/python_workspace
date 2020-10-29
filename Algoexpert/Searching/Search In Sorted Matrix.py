'''Search in Sorted Matrix

You're given a two-dimensonal array (a matrix) of distinct integers and a target integer. Each row in the matrix is sorted, and each column is also sorted; the matrix doesn't necessarily have the same height and width.

Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix, otherwise [-1,-1]
'''

# def searchInSortedMatrix(matrix, target):
#     # Write your code here.
#     ans = [(ix,iy) for ix,row in enumerate(matrix) for iy, i in enumerate(row) if i==target]
#     return ans[0] if ans else [-1,-1]

def searchInSortedMatrix(matrix, target):
    # Write your code here.
    row = 0
    col = len(matrix[row])-1
    length = len(matrix)
    while row < length and col >= 0:
        if target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
        else:
            return (row,col)
    return (-1,-1)

# --------------------------------------------

def searchInSortedMatrix(matrix, target):
    # Write your code here.
    col = -1
    length = target
    for row in range(length):
        print(len(matrix[row]),col,matrix[row][col])
        while target < matrix[row][col]:
            col -= 1
            if abs(col)>len(matrix[row]):
                return (-1,-1)
        while target > matrix[row][col]:
            break
        if target == matrix[row][col]:
            print(len(matrix[row]),col,matrix[row][col])
            return row,len(matrix[row])+col
    return (-1,-1)

matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]
target = 44

print(searchInSortedMatrix(matrix, target))