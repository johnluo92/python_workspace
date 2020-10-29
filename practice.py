class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = Node()

	def append(self, data):
		new_node = Node(data)
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = new_node

	def length(self):
		cur = self.head
		total = 0
		while cur.next:
			total += 1
			cur = cur.next
		return total

	def display(self):
		elems = []
		cur_node = self.head
		while cur_node.next:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

	def get(self, index):
		if index>= self.length():
			print("Error: 'Get' Index out of range!")
			return
		cur_index = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next
			if cur_index==index: return cur_node.data
			cur_index+=1

	def erase_node_of_index(self, index):
		if index >= self.length():
			print("Error: 'Get' Index out of range!")
			return
		cur_index=0
		cur_node=self.head
		while True:
			last_node = cur_node
			cur_node = cur_node.next
			if cur_index == index:
				last_node.next = cur_node.next
				return
			cur_index+=1


my_list = linked_list() 
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)


my_list.display()

my_list.erase_node_of_index(0)
my_list.display()

# ---------------------------------------------------------------------------------------
def getNthSmallest(arr, n):
    start = 0
    end = len(arr)-1
    newArr = [0 for i in range(len(arr))]
    
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            newArr[start] = arr[i]
            start += 1
        elif arr[i] > arr[0]:
            newArr[end] = arr[i]
            end -= 1
    
    newArr[start] = arr[0]
    print(n,start, newArr)
    if n < start+1:
        return getNthSmallest(newArr[:start], n)
    elif n > start+1:
        return getNthSmallest(newArr[start+1:], n-start-1)
    else:
        return newArr[start]
    
    # [2, 3, 5, 15, 11, 10, 4, 8]
    
    # [3, 5, 15, 11, 10, 4, 8]
    
    # [2, 3, 4, 5, 8, 10, 11, 15]
    
# [(0, 2), (1, 3), (2, 4), (3, 5), (4, 8), (5, 10), (6, 11), (7, 15), (8, 20)]

arr = [20, 2, 8, 4, 10, 11, 15, 5, 3]
n = 6

print(getNthSmallest(arr, n))