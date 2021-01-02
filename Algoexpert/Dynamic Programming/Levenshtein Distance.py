def levenshtein_distance(string1, string2):
    grid_2_d = [[i for i in range(len(string1) + 1)] for _ in range(len(string2) + 1)]

    for row in range(len(grid_2_d)):
        grid_2_d[row][0] = row
        for col in range(len(grid_2_d[row])):

            if row > 0 and col > 0:
                if string2[row - 1] == string1[col - 1]:
                    grid_2_d[row][col] = grid_2_d[row - 1][col - 1]

                else:
                    left = grid_2_d[row][col - 1]
                    top = grid_2_d[row - 1][col]
                    diagonal = grid_2_d[row - 1][col - 1]
                    total_edit = min(left, top, diagonal)
                    grid_2_d[row][col] = total_edit + 1

    total_distance = grid_2_d[len(string2)][len(string1)]
    print(f'total edits needed: {total_distance}')
    return total_distance


str1 = 'john testing for that'
str2 = 'jonh testing for this'
levenshtein_distance(str1, str2)
