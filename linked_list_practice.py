#https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/

class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def first_node(self):
		if self.head:
			cur_node = self.head
			return cur_node.data
		else:
			return 'empty LinkedList'

	def listed(self):
		myList = []
		head = self.head
		while head:
			myList.append(head.data)
			head = head.next
		return myList

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data, end=' ')
			cur_node = cur_node.next

	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node 

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def reverse(self):
		head = self.head
		prev = None

		while head:
			next_node = head.next
			head.next = prev
			prev = head
			head = next_node
		self.head = prev

			# print('cur_node: {}\nnext_node: {}\nprev: {}\n'.format(cur_node.data, next_node.data, prev.data))
			# return
	def node_of_index(self, index):
		head = self.head
		counter = 0
		while head:
			if counter == index:
				return head.data
			head = head.next
			counter+=1

	def length(self):
		head = self.head
		counter = 0
		while head.next:
			head = head.next
			counter += 1
		return counter

	def insert_node(self, data, index):
		head = self.head
		if index == 0:
			self.prepend(data)

		if index > self.length():
			self.append(data)
			return

		new_node = Node(data)
		counter = 1
		while head:
			if counter == index:
				pre = head.next
				head.next = new_node
				new_node.next = pre
			head = head.next
			counter+=1

	def remove_index(self, index):
		head = self.head
		if index >= self.length():
			return "index out of bound"
		if index == 0:
			self.head = head.next
			return
		head = self.head
		counter = 0
		prev = None
		while head:
			if counter == index:
				prev.next = head.next
				return
			prev = head
			head = head.next

	def intersect(self, headA, headB):
	    myList = []

	    while headA:
	        myList.append(headA.val)
	        headA = headA.next
	    while headB:
	        if headB.val in myList:
	            return headB
	        headB = headB.next
	    return None



# a = Node('a')
# b = Node('b')
# c = Node('c')

llist = LinkedList()
# llist.head = a
# llist.head.next = b
# b.next = c
# # print(llist.head.data)
# # print(a.next.next.data)
# while llist.head:
# 	print(llist.head.data)
# 	llist.head = llist.head.next

# print(llist.first_node())



llist.append('C')
llist.append('D')
llist.append('E')
llist.prepend('B')
llist.prepend('A')
llist.print_list()
print()
print('after reverse')
llist.reverse()
llist.print_list()
j = llist.node_of_index(4)
print('\n',j)

llist.insert_node('hi',5)
print(llist.length())
print()
llist.print_list()

llist.remove_index(0)
print()
llist.print_list()

print()
bList = LinkedList()
bList.append(1)
bList.append(llist.node_of_index(2))
bList.print_list()