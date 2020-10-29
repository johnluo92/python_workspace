def riverSizes(matrix):
    # Write your code here.
    traversed = [[False for i in range(len(matrix[0]))] for i in range(len(matrix))]
    ans = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if traversed[row][col]:
                continue
            else:
                sumOfThisRiver = dfsTravel(matrix, traversed, row, col, 0)
                if sumOfThisRiver != 0:
                    ans.append(sumOfThisRiver)
    return ans

def dfsTravel(matrix, traversed, row, col, sumTracker):
    if traversed[row][col]:
        return sumTracker
    traversed[row][col] = True

    if matrix[row][col] == 1:
        sumTracker += 1
    else:
        return sumTracker

    leftbound, upperbound = 0, 0
    rightbound, lowerbound = len(matrix[0]), len(matrix)
    
    # go left if possible
    if col-1 >= leftbound:
        sumTracker = dfsTravel(matrix, traversed, row, col-1, sumTracker)
    # go up if possible
    if row-1 >= upperbound:
        sumTracker = dfsTravel(matrix, traversed, row-1, col, sumTracker)
    # go right if possible
    if col+1 < rightbound:
        sumTracker = dfsTravel(matrix, traversed, row, col+1, sumTracker)
    # go down if possible
    if row+1 < lowerbound:
        sumTracker = dfsTravel(matrix, traversed, row+1, col, sumTracker)
    
    return sumTracker

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]

print(riverSizes(matrix))