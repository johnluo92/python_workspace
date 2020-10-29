'''Find Loop

Write a function that takes in the head of a Singly Linked List that contains a loop (in others words, the list's tail node points to some node in the list instead of None/null). The function should return the node (the actual node-not just its value) from which the loop originates in constant space.
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
		
def findLoop(head):
    # Write your code here.
	travelled = {}
    while head:
		if head not in travelled:
			travelled[head] = None
			head = head.next
		else:
			return head

