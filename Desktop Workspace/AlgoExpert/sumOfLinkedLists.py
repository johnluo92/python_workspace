# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#main function
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here
	listOne, listTwo = ''.join(reversed(getList(linkedListOne))), ''.join(reversed(getList(linkedListTwo)))
	print(listOne, listTwo)
	newNum = int(listOne) + int(listTwo)

    return getNewLinkedList(newNum)

def getList(linkedList):

	listFormat = []

	while linkedList is not None:
		listFormat.append(linkedList.value)
		linkedList = linkedList.next

	return listFormat

def getNewLinkedList(sumAnswer):
	#123 ==> 3-2-1

	prevNode = None
	for digit in reversed(str(sumAnswer)):
		newNode= LinkedList(int(digit))
		if prevNode is None:
			prevNode = firstNode = newNode
		else:
			prevNode.next, prevNode = newNode, newNode

	
	return firstNode