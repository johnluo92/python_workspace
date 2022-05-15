def minimumPassesOfMatrix(matrix):
    # Write your code here.
	negCount = 0
    for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			value = matrix[row][col]
			if value < 0:
				negCount += 1
	return getPassCount(matrix, negCount)

def getPassCount(matrix, negCount):
	totalPass, convertables = 0, []
	print(negCount)

	while negCount > 0:

	    for row in range(len(matrix)):
			for col in range(len(matrix[row])):
				if matrix[row][col] < 0:
					if canConvert(matrix, row, col):
						convertables.append([row,col])

		print(convertables)
		if negCount != 0 and len(convertables) == 0:
			return -1

		for coordinates in convertables:
			row, col = coordinates
			matrix[row][col] = abs(matrix[row][col])
			negCount -= 1
		convertables = []

		totalPass += 1

	return totalPass

def canConvert(matrix, row, col):

	if col-1 >= 0:
		if matrix[row][col-1] > 0:
			return True
	if row-1 >= 0:
		if matrix[row-1][col] > 0:
			return True
	if col+1 < len(matrix[row]):
		if matrix[row][col+1] > 0:
			return True
	if row+1 < len(matrix):
		if matrix[row+1][col] > 0:
			return True

	return False