def zigzagTraverse(array):
    
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    
    output = traverse_graph(array, [])
    return output

def traverse_graph(array, output):
    down = True
    output = []
    output.append(array[0][0])
    i, j = 0, 0
    while i != len(array)-1 or j != len(array[0])-1:
        if down:
            # go down left
            while i+1 < len(array) and j -1 >= 0:
                i += 1
                j -= 1
                output.append(array[i][j])
            # can go down
            if i + 1 < len(array):
                i += 1
                output.append(array[i][j])
                down = False
            # can go right
            elif j + 1 < len(array[0]):
                down = False
                j += 1
                output.append(array[i][j])
        if not down:
            # can go up right
            while i -1 >= 0 and j + 1 < len(array[0]):
                i -= 1
                j += 1
                output.append(array[i][j])
            # if can go right
            if j + 1 < len(array[0]):
                j += 1
                output.append(array[i][j])
                down = True
            # if can go down
            elif i + 1 < len(array):
                down = True
                i += 1
                output.append(array[i][j])
                # output.append('test')

    return output
  

array =    [[1, 3, 4, 10],
            [2, 5, 9, 11],
            [6, 8, 12, 15],
            [7, 13, 14, 16]]

print(zigzagTraverse(array))

