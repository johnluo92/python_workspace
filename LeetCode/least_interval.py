import sys

class Solution:
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)
        
        my_tasks = {k:tasks.count(k) for k in tasks}
        a = list(my_tasks.items())
        a.sort(key = lambda x: x[1], reverse = True)
        my_tasks = {k:v for k,v in a}

        cannot_use = {}
        ans = []

        while len(my_tasks):            

            task = self.get_next_task(my_tasks, cannot_use, n)

            ans.append(task)
            # print(my_tasks)
            # sys.exit(0)

            print('ans:',ans)

            # if len(ans) == 10:
            #     print(my_tasks)
            #     sys.exit(0)
        print('answer: ', len(ans))
        return len(ans)

    def get_next_task(self, my_tasks, cannot_use, n):
        next_task = None
        found_key = False
        evict_list = []

        if len(cannot_use) == 0:

            task = list(my_tasks.keys())[0]

            my_tasks[task] -= 1

            cannot_use[task] = n

            if my_tasks[task] == 0:
                my_tasks.pop(task)

            return task

        else:
            for key in my_tasks:
                if key in cannot_use:
                    cannot_use[key] -= 1
                    if cannot_use[key] == 0:
                        cannot_use.pop(key)
                    continue
                else:
                    if not found_key:
                        found_key = True
                        cannot_use[key] = n
                        next_task = key
                        my_tasks[key] -= 1
                        if my_tasks[key] == 0:
                            evict_list.append(key)
        for key in evict_list:
            my_tasks.pop(key)
        print('\ncannot:',next_task, cannot_use, my_tasks)
        return next_task

tasks = ["A","B","B","B","B"]
tasks = ["A","A","A","B","B","B"]
t = 2
tasks = ["A","B","C","D","E","A","B","C","D","E"]
t = 4
tasks = ["A","A","A", "B","B","B", "C","C","C", "D", "D", "E"]
t = 2
# B-A-X-B-X-X-B-X-X-B 10

Solution().leastInterval(tasks,t)