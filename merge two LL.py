# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    
    # 6 head1 -> 7 -> 8 -> 9 -> 10
    # 1 head2 -> 3 -> 4 -> 5
    
    # 1 prev -> 6 head1 -> 7 -> 8 -> 9 -> 10
    # 3 head2-> 4 -> 5
    head1 = headOne
    head2 = headTwo
    if head1.value <= head2.value:
        ans = headOne
    else:
        ans = headTwo
    prev = None
    while head1 and head2:
        if head2.value < head1.value:
            temp2 = head2.next
            head2.next = head1
            if not prev:
                prev = head2
            else:
                prev.next = head2
                prev = head2
            head2 = temp2
        elif head2.value >= head1.value:
            prev = head1
            head1 = head1.next
            
    if not prev.next:
        prev.next = head2
    
    return ans

    # 6 -> 7 -> 8 -> 9 -> 10
    # 1 -> 3 -> 4 -> 5
    
one = LinkedList(6)
one.next = LinkedList(7)
one.next.next = LinkedList(8)
one.next.next.next = LinkedList(9)
one.next.next.next.next = LinkedList(10)

two = LinkedList(1)
two.next = LinkedList(3)
two.next.next = LinkedList(4)
two.next.next.next = LinkedList(5)
two.next.next.next.next = LinkedList(9)
two.next.next.next.next.next = LinkedList(10)

# one = LinkedList(1)
# one.next = LinkedList(2)

# two = LinkedList(1)
# two.next = LinkedList(1.5)

ans = mergeLinkedLists(one, two)

while ans:
    print(ans.value)
    ans = ans.next