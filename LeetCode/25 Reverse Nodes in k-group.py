# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        
        counter = 0
        myArr = [None for i in range(k)]
        beg = None
        node = head
        ans = []
        
        while node:
            myArr[counter] = node
            node = node.next
            counter += 1
            if counter == k:
                self.reverseMyArr(myArr)
                newHead = myArr[-1]
                newTail = myArr[0]
                if beg is not None:
                    beg.next = newHead
                else:
                    head = newHead
                newTail.next = node
                beg = newTail
                counter = 0
    
        self.print_LL(head, ans)
        print(ans)
        return ans
    
    def reverseMyArr(self, nodesToReverse):
        head = nodesToReverse[0]
        prev = head
        head = head.next
        i = 1
        while i < len(nodesToReverse):
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
            i += 1
            
    def print_LL(self, head, array):
        while head:
            array.append(head.val)
            head = head.next


newLL = ListNode(1)
newLL.next = ListNode(2)
newLL.next.next = ListNode(3)
newLL.next.next.next = ListNode(4)
newLL.next.next.next.next = ListNode(5)

# 1 -> 2 -> 3 -> 4 -> 5

newSolution = Solution()
newSolution.reverseKGroup(newLL, 2)

newLL2 = ListNode(1)
newLL2.next = ListNode(2)

newSolution2 = Solution()
newSolution2.reverseKGroup(newLL2, 2) # 2 -> 1