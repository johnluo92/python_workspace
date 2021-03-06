def topologicalSort(tasks, dependencyList):
    # Write your code here.
    myGraph = Graph(tasks, dependencyList)
    print(myGraph.dependencies)
    myGraph.createTaskOrder()
    return list(myGraph.answer.keys())


class Graph:
    def __init__(self, tasks, dependencyList):
        self.dependencies = {key: [] for key in tasks}
        self.traversing = set()
        self.answer = {}

        self.populateDependecies(dependencyList)

    def populateDependecies(self, tasks):
        for dep, task in tasks:
            self.dependencies[task].append(dep)

    def createTaskOrder(self):
        for job in self.dependencies:
            if self.canTraverseGraph(job):
                continue
            else:
                self.answer = {}
                return

    def dfsTraverseGraph(self, job):
        if not len(self.dependencies[job]):
            self.answer[job] = None
            return True
        else:
            while len(self.dependencies[job]):
                task = self.dependencies[job].pop(0)
                if self.canTraverseGraph(task):
                    continue
                else:
                    return False
            if not len(self.dependencies[job]):
                self.answer[job] = None
            return True

    def canTraverseGraph(self, current_job):
        print('answer set:', self.answer)
        print('traversing set:', self.traversing)
        if current_job in self.answer:
            return True
        elif current_job not in self.traversing:
            self.traversing.add(current_job)
            if self.dfsTraverseGraph(current_job):
                if current_job in self.traversing:
                    self.traversing.remove(current_job)
                return True
        return False


jobs = [1, 2, 3, 4]
deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
answer = topologicalSort(jobs, deps)
print(answer)
