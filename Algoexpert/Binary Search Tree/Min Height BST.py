'''Min Height BST

Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers, and returns the root of the BST.

The function should minimize the height of the BST.

'''

# o(n) time | o(n) space
def minHeightArray(array, newarray):
    if len(array) == 0:
        return array
    else:
        mid = (len(array) // 2)
        newarray.append(array[mid])
        minHeightArray(array[:mid],newarray)

    minHeightArray(array[mid+1:],newarray)
    return newarray

def minHeightBst(array):
    newArray = []
    insertArray = minHeightArray(array, newArray)
    print('Queue of list to insert:', insertArray)
    myTree = BST(insertArray.pop(0))
    while len(insertArray) > 0:
        myTree.insert(insertArray.pop(0))
    return myTree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


print(minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22])) # True