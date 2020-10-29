# Create the Node class
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

# Create the doubly linked list
class doubly_linked_list:

   def __init__(self):
      self.head = None

# Define the push method to add elements		
   def prepend(self, NewVal):

      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode

# Define the append method to add elements at the end
   def append(self, NewVal):

      NewNode = Node(NewVal)
      NewNode.next = None
      if self.head is None:
         NewNode.prev = None
         self.head = NewNode
         return
      last = self.head
      while (last.next is not None):
         last = last.next
      last.next = NewNode
      NewNode.prev = last
      return

# Define the insert method to insert the element		
   def insert(self, prev_node, NewVal):
      if prev_node is None:
         return
      NewNode = Node(NewVal)
      NewNode.next = prev_node.next
      prev_node.next = NewNode
      NewNode.prev = prev_node
      if NewNode.next is not None:
         NewNode.next.prev = NewNode

# Define the method to print the linked list 
   def listprint(self):
        l = []
        head = self.head
        while head:
            l.append(head.data)
            head = head.next
        print(l)
    
dllist = doubly_linked_list()
dllist.prepend(12)
dllist.prepend(8)
dllist.prepend(62)
dllist.insert(dllist.head.next, 13)
dllist.listprint()