'''
river sizes
matrix traversal

count the adjacent rivers and their total sizes and return a list of the sizes
https://www.algoexpert.io/questions/River%20Sizes

my solution: calling the main function riverSizes returning the result
the result will be return from traversing the map whilst checking for 
traversed river 'nodes' and marking them as checked. If a river node is a 1
then the traverseRiver function will algorithmically traverse the matrix
using the bounds set as conditions for when to stop increasing/decreasing row/col.

These bounds are established everytime the algorithm is called and returns an additional
length of 1 if that node is a river node. Returning the length of the total rivers counted
to each matrix cell (whilst recursively marking them as traversed and continue whilst the next iteration
touches on an already traversed node)'''

def riverSizes(matrix):
    # Write your code here.
    res = []
    checkedMatrix = [[False for value in row] for row in matrix]
    print(checkedMatrix)
    traverseMap(matrix, checkedMatrix, res)
    return res

def traverseMap(matrix, checkedMatrix, res):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            curLen = 0
            curLen = traverseRiver(row, col, checkedMatrix, matrix, curLen)
            if curLen:
                res.append(curLen)

def traversed(row, col, checkedMatrix):
    if checkedMatrix[row][col]:
        return True
    else:
        checkedMatrix[row][col] = True
        return False

def traverseRiver(row, col, checkedMatrix, matrix, curLen):
    leftbound, upperbound = 0, 0
    rightbound, lowerbound = len(matrix[0])-1, len(matrix)-1

    if not traversed(row, col, checkedMatrix):
        if matrix[row][col] != 1:
            return curLen
        curLen += 1
        #up
        if row-1 >= upperbound:
            curLen = traverseRiver(row-1, col, checkedMatrix, matrix, curLen)
        #down
        if row+1 <= lowerbound:
            curLen = traverseRiver(row+1, col, checkedMatrix, matrix, curLen)
        #left
        if col-1 >= leftbound:
            curLen = traverseRiver(row, col-1, checkedMatrix, matrix, curLen)
        #right
        if col+1 <= rightbound:
            curLen = traverseRiver(row, col+1, checkedMatrix, matrix, curLen)
    return curLen

mat = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]

# mat = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]

# mat = [
#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [1, 0, 1, 1, 1, 1, 0, 1],
#     [0, 1, 1, 0, 0, 0, 1, 1]
#   ]


ans = riverSizes(mat)
print('answer', ans)