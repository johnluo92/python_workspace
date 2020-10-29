def riverSizes(matrix):
    # Write your code here.
    res = []
	checkedMatrix = [[False for col in matrix[0]] for row in matrix]
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