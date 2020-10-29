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

# problem 3 -> 0 -> 5 -> 2 -> 1 -> 4

# result  0 -> 2 -> 1 -> 3 -> 5 -> 4
        
my_LL = LinkedList(6)
my_LL.next = LinkedList(0)
my_LL.next.next = LinkedList(5)
my_LL.next.next.next = LinkedList(2)
my_LL.next.next.next.next = LinkedList(1)
my_LL.next.next.next.next.next = LinkedList(4)

print(rearrangeLinkedList(my_LL, 3))-