def zigzagTraverse(array):
    # Write your code here.
	output = []

	arrayNodes = len(array) * len(array[0])
	traversed = [[False for col in row] for row in array]
	
	upperbound, leftbound = 0, 0
	lowerbound, rightbound = len(array), len(array[0])
	i, j = 0, 0

	while len(output) < arrayNodes:
		
		if i == 0 and j == 0:
			traversed[i][j] = True
			output.append(array[i][j])
		
		# down once within lowerbound		
		if i+1<lowerbound:
			i += 1
			traversed[i][j] = True
			output.append(array[i][j])
		
		# upright till upperbound/rightbound
		while i-1 >= upperbound and j+1 < rightbound and not traversed[i-1][j+1]:
			i -= 1
			j += 1
			traversed[i][j] = True
			output.append(array[i][j])
		
		# right once within rightbound
		if j+1 < rightbound:
			j += 1
			traversed[i][j] = True
			output.append(array[i][j])
		
		# downleft till lowerbound/leftbound
		if i != upperbound or j != rightbound-1:
			while i+1 < lowerbound and j-1 >= leftbound and not traversed[i+1][j-1]:
				i += 1
				j -= 1
				traversed[i][j] = True
				output.append(array[i][j])
		print(output)
	return output

array = [[1, 3,  4,  10],
		 [2, 5,  9,  11],
		 [6, 8,  12, 15],
		 [7, 13, 14, 16]]

array = [[1, 3, 4, 7, 8],
		 [2, 5, 6, 9, 10]]

zigzagTraverse(array)