'''Remove K-th Node from End

Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end of the list.

The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).

Furthermore, the input head of the linked list should remain the head of the linked list after the removeal is done, even if the head is the node that's supposed to be removed. In other words, if the head is the node that's supposed to be removed, your function should simply mutate its value and next pointer.

The linked list will always have at least two nodes and, more specifically, at least k nodes.
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    originalHead = head.value
    end = head
    i = 0
    while k-i > 1:
        if end.next:
            end = end.next
        i += 1

    prev = head
    while end.next:
        prev = head
        head = head.next
        end = end.next

    print('node with value {} to be removed'.format(head.value))
    if prev != head:
        prev.next = head.next
        head.next = None
    else:
        head.value = head.next.value
        nextNode = head.next
        head.next = nextNode.next
        nextNode.next = None
        del nextNode

headNode = LinkedList(0)
headNode.next = LinkedList(1)
headNode.next.next = LinkedList(2)
headNode.next.next.next = LinkedList(3)
headNode.next.next.next.next = LinkedList(4)
headNode.next.next.next.next.next = LinkedList(5)
headNode.next.next.next.next.next.next = LinkedList(6)
headNode.next.next.next.next.next.next.next = LinkedList(7)
headNode.next.next.next.next.next.next.next.next = LinkedList(8)
headNode.next.next.next.next.next.next.next.next.next = LinkedList(9)
k = 10

node = headNode
while node:
	print(node.value, end=' ')
	node = node.next

print()
removeKthNodeFromEnd(headNode, k)

node = headNode
while node:
	print(node.value, end=' ')
	node = node.next