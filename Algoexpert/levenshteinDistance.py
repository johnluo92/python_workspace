def levenshteinDistance(str1, str2):
    # Write your code here.
    grid2D = [[i for i in range(len(str1)+1)] for x in range(len(str2)+1)]

    for row in range(len(grid2D)):
        grid2D[row][0] = row
        for col in range(len(grid2D[row])):
            
            
            if row>0 and col>0:
                if str2[row-1] == str1[col-1]:
                    grid2D[row][col] = grid2D[row-1][col-1]
                    
                else:
                    edit = min(grid2D[row][col-1],grid2D[row-1][col],grid2D[row-1][col-1])
                    grid2D[row][col] = edit+1
            
            
            print(grid2D[row][col], end='  ')
        print()
        
    LD = grid2D[len(str2)][len(str1)]
    print(LD)
    return LD

    
str1 = 'john luo has a low level understanding of the things in lives'
str2 = 'john luo has a high level understanding of the things in life'
levenshteinDistance(str1, str2)