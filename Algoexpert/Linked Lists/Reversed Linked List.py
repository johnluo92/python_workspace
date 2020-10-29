def reverseLinkedList(head):
    # Write your code here.
	prev = head
	head = head.next
	prev.next = None
    while head is not None:
		nextNode = head.next
		head.next = prev
		prev = head
		head = nextNode
	
	return prev