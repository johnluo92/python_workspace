image = [[1,2,3],
		 [4,5,6],
		 [7,8,9]]

image2 = [[i for i in range(1,5)],[i for i in range(5,9)],[i for i in range(9,13)],[i for i in range(13,17)]]
print(image2)
#         transposed
#         [1,4,7]
#         [2,5,8]
#         [3,6,9]

#         result
#         [7,4,1]
#         [8,5,2]
#         [9,6,3]

def rotate(image):
	n = len(image)
	for row in range(n):
		for col in range(row,n):
			temp = image[row][col]
			image[row][col] = image[col][row]
			image[col][row] = temp

	for row in range(n):
		for col in range(n//2):
			temp = image[row][col]
			image[row][col] = image[row][-1-col]
			image[row][-1 - col] = temp

	return image

result = rotate(image2)
print()
for i in result:
    print(i)