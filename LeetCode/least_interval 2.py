import sys
from queue import PriorityQueue
import heapq

my_arr = [[4, 'Read'],[2, 'Play'],[5, 'Write'],[1, 'Code'],[3, 'Study']]

heapq.heapify(my_arr)
heapq._heapify_max(my_arr) 

# q = PriorityQueue()

# q.put([4, 'Read'])
# q.put([2, 'Play'])
# q.put([5, 'Write'])
# q.put([1, 'Code'])
# q.put([3, 'Study'])

# while not q.empty():
#     next_item = q.get()
#     # print(next_item)

class Solution:
    def leastInterval(self, tasks, n):

        freq_of_tasks = {k:tasks.count(k) for k in tasks}
        my_tasks = []
        for k,v in freq_of_tasks.items():
            my_tasks.append([v,k])

        heapq.heapify(my_tasks)
        heapq._heapify_max(my_tasks)
        cannot_use = {}
        temp = {}

        task_list = []
        while len(my_tasks) or len(temp):

            task = self.getTask(my_tasks, cannot_use, temp, n)

            task_list.append(task)

            print(task_list, temp, cannot_use)

        print('answer:', len(task_list))
        return len(task_list)


    def getTask(self, my_tasks, cannot_use, temp, n):
        task, temp2, val = None, None, None
        if len(cannot_use) == 0:
            task = heapq._heappop_max(my_tasks)
            task[0] = task[0]-1
            if task[0] != 0:
                temp[task[1]] = task[0]
                cannot_use[task[1]] = n
            return task[1]
        else:
            for job in cannot_use:
                if cannot_use[job] > 0:
                    cannot_use[job] -= 1
                if cannot_use[job] == 0:
                    temp2 = job
            if temp2 is not None:
                cannot_use.pop(temp2)
                val = temp.pop(temp2)
            if len(my_tasks) > 0:
                if val is not None:
                    my_tasks.append([val, temp2])
                    val = None
                print(my_tasks)
                task = heapq._heappop_max(my_tasks)
                task[0] = task[0]-1
                if task[0] != 0:
                    temp[task[1]] = task[0]
                    cannot_use[task[1]] = n
            if val is not None:
                my_tasks.append([val, temp2])  

        return task[1] if task else None


# tasks = ["A",'A']
# t = 2 # ans = 4 b-a-_b

# tasks = ["A","A","A","B","B","B"]
# t = 2 # ans = 8
# #  # ans = max(len(tasks), (max_freq + 1) * (n - 1) + count_of_max_freq
# #  # ans = max(6, ((3-1) * (2+1) + 2)) = 8

# tasks = ["A","B","C","D","E","A","B","C","D","E"]
# t = 4
# #  # ans = max(len(tasks), (max_freq -1 ) * (n +1) + count_of_max_freq)
# #  # ans = max(10, (2 - 1) * (4 + 1) + 5) = 10


# tasks = ["A","A","A", "B","B","B", "C","C","C", "D", "D", "E"]
# t = 2
# #  # ans = max(12, (2) * (3) + 3) = 12

# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
# t = 2
 # ans = max(12, (6-1)*(2+1) + 1) = 16

tasks = ["A","A","A"]
t = 1

Solution().leastInterval(tasks,t)