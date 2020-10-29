'''Youngest Common Ancestor

You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor property pointing to their youngst ancestor. The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor -- its ancestor is null/None), and the other two inputs are descendants in the ancestral tree.

Write a function that returns the youngest common ancestor to the two descendants.
'''

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
	head1, head2 = descendantOne, descendantTwo
	queue1, queue2 = [], []
	while head1:
		queue1.append(head1)
		head1 = head1.ancestor
	while head2:
		queue2.append(head2)
		head2 = head2.ancestor
	
	while len(queue1) > len(queue2):
			queue1.pop(0)
	while len(queue2) > len(queue1):
			queue2.pop(0)
	
	while len(queue1) and len(queue2):
		ancestor = queue1[0]
		if queue1.pop(0) == queue2.pop(0):
			print(ancestor.name)
			return ancestor
	print(topAncestor.name)
	return topAncestor

E = AncestralTree('E')
E.ancestor = AncestralTree('B')
E.ancestor.ancestor = AncestralTree('A')
I = AncestralTree('I')
I.ancestor = AncestralTree('D')
I.ancestor.ancestor = E.ancestor

print(getYoungestCommonAncestor(None, E, I)) # True