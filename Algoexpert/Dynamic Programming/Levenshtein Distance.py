def levenshteinDistance(str1, str2):
    grid2D = [[i for i in range(len(str1)+1)] for x in range(len(str2)+1)]

    for row in range(len(grid2D)):
        grid2D[row][0] = row
        for col in range(len(grid2D[row])):
            
            
            if row>0 and col>0:
                if str2[row-1] == str1[col-1]:
                    grid2D[row][col] = grid2D[row-1][col-1]
                    
                else:
                    left = grid2D[row][col-1]
                    top  = grid2D[row-1][col]
                    upleft = grid2D[row-1][col-1]
                    totalEdit = min(left, top, upleft)
                    grid2D[row][col] = totalEdit+1
        
    LD = grid2D[len(str2)][len(str1)]
    print(f'total edits needed: {LD}')
    return LD

    
str1 = 'john testing for that'
str2 = 'jonh testing for this'
levenshteinDistance(str1, str2)