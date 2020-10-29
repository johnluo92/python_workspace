'''Linked List Construction

methods will include the following:
- setting the head
- setting the tail
- inserting before a node
- inserting after a node
- insertAtPosition
- removeNodesWithValue
- remove
- containsNodeWithValue
'''

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        # empty DLL
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)
        
    def setTail(self, node):
        # Write your code here.
        # empty DLL
        if not self.tail:
            self.setHead(node)
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if not node.prev:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if not node.next:
            self.tail = nodeToInsert
        else:
            node.next = nodeToInsert
        node.next.prev = nodeToInsert
        
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return
        else:
            counter = 1
            head = self.head
            while head and position != counter:
                counter += 1
                head = head.next
            if not head:
                self.setTail(nodeToInsert)
            else:
                self.insertBefore(head, nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        head = self.head
        while head:
            nodeToRemove = head
            head = head.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
                    
    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        # Write your code here.
        head = self.head
        while head and head.value != value:
            head = head.next
        return head is not None
    
    def removeNodeBindings(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
