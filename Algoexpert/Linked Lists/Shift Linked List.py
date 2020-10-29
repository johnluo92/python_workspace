'''Shift Linked List

Write a function that takes in the head of a Singly Linked List and an integer k, shifts the list in place (i.e. doesn't create a brad new list) by k position, and returns its new head.

Shifting a Linked List means moving its nodes forward or backward and wrapping them around the list where appropriate. For example, shifting a Linked List forward by one position would make its tail become the new head of the linked list.

Whether nodes are moved forward or backward is determined by wehether k is positive or negative.
'''

def shiftLinkedList(head, k):
    # Write your code here.    
    if k == 0:
        return head
    
    length = 0
    testLen = head
    while testLen:
        length += 1
        testLen = testLen.next
        
    k = k % length
    if k == 0:
        return head
        
    counter = 0
    end = head
    newEnd = head
    
    while counter != k:
        end = end.next
        counter += 1
    
    while end.next:
        newEnd = newEnd.next
        end = end.next
    newHead = newEnd.next
    end.next = head
    newEnd.next = None
    return newHead
