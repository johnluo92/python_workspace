#graph learning DFS

class myGraph:
	def __init__(self, edges):
		self.vertices = dict.fromkeys((sum(edges,[])),False)
		self.graph = {}
		for fro, to in edges:
			if fro not in self.graph:
				self.graph[fro] = [to]
			else:
				self.graph[fro].append(to)

		print(self.vertices)
		print()
		print(self.graph)

	def DFS_Traverse(self, head):
		self.vertices[head] = True
		print(head)
		if head in self.graph:
			for vertex in self.graph[head]:
				if self.vertices[vertex] == False:
					self.DFS_Traverse(vertex)

	def print_traveled(self):
		print(self.vertices)
		print(list(dict.values(self.vertices)).count(False))
		return list(dict.values(self.vertices)).count(False)


# entries = int(input())
# edges = []
# for i in range(entries):
#     edge = input()
#     edges.append(edge.split(' '))
edges = [['8', '1'],['8', '3'],['7', '4'],['7', '5'],['2', '6'],
['10', '7'],['2', '8'],['10', '9'],['2', '10'],['5', '10']]
newGraph = myGraph(edges)
newGraph.DFS_Traverse('2')
newGraph.print_traveled()