def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    maxTotal = float('-inf')

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            runningTotal = getRunningTotal(matrix, row, col, size)
            maxTotal = max(maxTotal, runningTotal)
            print(maxTotal)
    return maxTotal

def getRunningTotal(matrix, row, col, size):
    runningTotal = float('-inf')

    xBound, yBound = col+size, row+size
    if yBound <= len(matrix) and xBound <= len(matrix[row]):
        runningTotal = 0
        for y in range(row, yBound):
            for x in range(col, xBound):
                runningTotal += matrix[y][x]
                print("current row: {} \nCurrent col: {} \nrunningTotal: {}".format(y, x, runningTotal))

    return runningTotal

    