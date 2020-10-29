# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.

class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.cache = {}
        self.LinkedList = None

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if self.currentSize == 0:
            self.LinkedList = DoublyLinkedList()
            self.cache[key] = self.LinkedList.appendNode([key,value])
            self.currentSize += 1
        
        if key in self.cache:
            node = self.cache[key]
            if value != node.value[1]:
                self.cache[key] = self.LinkedList.makeNodeRecent(node, [key,value])
        else:
            if self.currentSize < self.maxSize:
                self.cache[key] = self.LinkedList.appendNode([key,value])
                self.currentSize += 1
            else:
                self.cache[key] = self.LinkedList.appendNode([key,value])
                prevHead = self.LinkedList.head
                self.LinkedList.head = prevHead.next
                self.cache.pop(prevHead.value[0])
                self.LinkedList.head.prev = None
                del prevHead
            
    def getValueFromKey(self, key):
        # Write your code here.
        if key in self.cache:
            node = self.cache[key]
            self.LinkedList.makeNodeRecent(node, [node.value[0],node.value[1]])
            value = node.value[1]
        else:
            return None
        return value

    def getMostRecentKey(self):
        # Write your code here.
        node = self.LinkedList.tail
        return node.value[0]
        
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def appendNode(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return self.head
        else:
            newTail = Node(value)
            self.tail.next = newTail
            newTail.prev = self.tail
            self.tail = newTail
            return self.tail
            
    def removeLRUNode(self):
        head = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        del head
        
    def makeNodeRecent(self, node, value):
        if node.prev is None and node.next:
            self.head = self.head.next
            self.head.prev = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None
            
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None
        
        self.tail.value = value
        return self.tail