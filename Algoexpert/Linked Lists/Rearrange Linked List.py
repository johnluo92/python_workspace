'''Rearrange Linked List

Write a function that takes in the head of a Singly Linked List and an integer k, rearranges the list in place (i.e., doesn't create a brand new list) around nodes with k, and returns its new head.

Rearranging a linked list around nodes with value k, means moving all nodes with a value smaller than k before all nodes with value k and moving all nodes with a value greater than k after all nodes with value k.

All moved nodes should maintain their original relative ordering if possible.

Note that the linked list should be rearranged even if it doesn't have any nodes with value k.
'''

# This is an input class. Do not edit.

def rearrangeLinkedList(head, k):
    # Write your code here.
    k_small = []
    k_nodes = []
    k_large = []
    while head:
        print(head.value)
        if head.value == k:
            k_nodes.append(head)
        elif head.value < k:
            k_small.append(head)
        else:
            k_large.append(head)
        prev = head
        head = head.next
        prev.next = None
            
    print('small: '  ,k_small)
    print()
    print('equals:'   ,k_nodes)
    print()
    print('larger:'   ,k_large)
    a = joinLists(k_small)
    b = joinLists(k_nodes)
    c = joinLists(k_large)
    
    ans = None
    ans = joinAll(a,b,c)
    
    head = ans
    while head:
        print(head.value, end = '')
        head = head.next
        
    return ans

def joinLists(node_list):
    if len(node_list):
        og = node_list[0]
        head = og
        i = 1
        while i < len(node_list):
            head.next = node_list[i]
            head = node_list[i]
            i += 1
        return og
    
def joinAll(a,b,c):
    if a:
        head = a
        prev = head
        while head:
            prev = head
            head = head.next
        if b:
            prev.next = b
        else:
            prev.next = c
    
    if b:
        head = b
        prev = head
        while head:
            prev = head
            head = head.next
        if c:
            prev.next = c
        
    if a:
        return a
    elif b:
        return b
    else:
        return c

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

print(xxxxx())