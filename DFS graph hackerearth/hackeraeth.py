'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
class myGraph:
	def __init__(self, edges):
		self.vertices = dict.fromkeys((sum(edges,[])),False)
		self.graph = {}
		for fro, to in edges:
			if fro not in self.graph:
				self.graph[fro] = [to]
			else:
				self.graph[fro].append(to)
			if to not in self.graph:
				self.graph[to] = [fro]
			else:
				self.graph[to].append(fro)

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

	def print_traveled(self, vertices, value):
		unknownVerticesNum = vertices - len(self.vertices)
		self.DFS_Traverse(value)
		ans = unknownVerticesNum+list(dict.values(self.vertices)).count(False)
		print('num of vertices:, ', len(self.vertices))
		print('untraveled/unvisited vertices: ', ans)

if __name__ == "__main__":
    entries = input('enter vertices and edges: ').split(' ')
    print(entries)
    vertices = int(entries[0])
    entries = int(entries[1])
    print('entries: ', entries)
    edges = []
    for i in range(int(entries)):
        edge = input()
        edges.append(edge.split(' '))
    newGraph = myGraph(edges)
    print('num of vertices: ', len(newGraph.vertices), '\n', newGraph.vertices)
    newGraph.print_traveled(vertices, input('head: '))
    print(newGraph.vertices)
