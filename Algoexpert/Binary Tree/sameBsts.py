def sameBsts(arrayOne, arrayTwo):
	print(arrayOne)
	print(arrayTwo)
	if len(arrayOne) == 0 or len(arrayTwo) == 0:
		return True
	if len(arrayOne) != len(arrayTwo):
		return False
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	arrOneSmaller = getSmaller(arrayOne)
	print(arrOneSmaller)
	arrTwoSmaller = getSmaller(arrayTwo)
	print(arrTwoSmaller)
	quit()
	arrOneBigger = getBigger(arrayOne)
	arrTwoBigger = getBigger(arrayTwo)
	
	return sameBsts(arrOneSmaller, arrTwoSmaller) and sameBsts(arrOneBigger, arrTwoBigger)

def getSmaller(inputArr, outputArr = []):
	for i in range(1, len(inputArr)):
		if inputArr[0] > inputArr[i]:
			outputArr.append(inputArr[i])
	return outputArr
		
def getBigger(inputArr):
	outputArr = []
	for i in range(1, len(inputArr)):
		if inputArr[0] <= inputArr[i]:
			outputArr.append(inputArr[i])
	return outputArr

arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

sameBsts(arrayOne, arrayTwo)