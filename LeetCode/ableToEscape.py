def ableToEscape(matrix, start, end, path = []):

    row, col = start
    endRow, endCol = end
    
    if matrix[row][col] == 0 and matrix[endRow][endCol] == 0:
        traversed = [[False for col in row] for row in matrix]
        traversed[row][col] = True
    else:
        return False

    findEscapeRoute(matrix, traversed, start, end, path)
    for row in traversed:
        print(row)
    
    print()
    print(path)

    return path if len(path) else False

def findEscapeRoute(matrix, traversed, start, end, path):
    if start == end:
        return True
    length, width = len(matrix), len(matrix[0])
    row, col = start
    direction = ['down', 'right', 'up', 'left']
    i = 0

    for x,y in ((1,0), (0,1), (-1,0), (0,-1)):
        new_row, new_col = row+x, col+y
        if new_row >= 0 and new_row < length and new_col >= 0 and new_col < width:
            if matrix[new_row][new_col] == 0 and not traversed[new_row][new_col]:
                traversed[new_row][new_col] = True
                path.append((direction[i]))
                if not findEscapeRoute(matrix, traversed, [new_row,new_col], end, path):
                    path.pop()
                else:
                    return True
        i+=1
    return False

matrix =   [[0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]]

# ---------------------------------------------------------------------------

# shortest path

def ableToEscape(matrix, start, end, path = []):

    row, col = start
    endRow, endCol = end
    myMatrix = [[0 if col == 0 else float('inf') for col in row] for row in matrix]
    
    if myMatrix[row][col] == 0 and myMatrix[endRow][endCol] == 0:
        traversed = [[False for col in row] for row in matrix]
        traversed[row][col] = True
    else:
        return False

    findShortestEscapeRoute(myMatrix, traversed, start, end, path)
    for row in traversed:
        print(row)
    
    print()
    print(path)

    return path if len(path) else False

def findEscapeRoute(matrix, traversed, start, end, path):
    queue = [(row,col)]
        return True
    length, width = len(matrix), len(matrix[0])
    row, col = start
    direction = ['down', 'right', 'up', 'left']
    i = 0

    for x,y in ((1,0), (0,1), (-1,0), (0,-1)):
        new_row, new_col = row+x, col+y
        if new_row >= 0 and new_row < length and new_col >= 0 and new_col < width:
            if matrix[new_row][new_col] == 0 and not traversed[new_row][new_col]:
                traversed[new_row][new_col] = True
                path.append((direction[i]))
                if not findEscapeRoute(matrix, traversed, [new_row,new_col], end, path):
                    path.pop()
                else:
                    return True
        i+=1
    return False

matrix =   [[0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]]

ableToEscape(matrix, [0,4], [4,4]) #find the path

