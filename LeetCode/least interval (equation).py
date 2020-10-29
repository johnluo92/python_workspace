class Solution:
    def leastInterval(self, tasks, n):

        if n == 1:
            ans = len(tasks)
            print(ans)
            return ans

        my_dict = {k:tasks.count(k) for k in tasks}
        job_freqs = sorted(list(my_dict.values()), reverse = True)

        most_occurring = job_freqs[0]
        count_most_occ = job_freqs.count(most_occurring)

        ans = max(len(tasks), ((most_occurring-1) * (n+1) + count_most_occ))

        print(ans)
        return ans


tasks = ["A","B","B","B","B"]
t = 1 # ans = 5
tasks = ["A","A","A","B","B","B"]
t = 2 # ans = 8
 # ans = max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq
 # ans = max(6, ((3-1) * (2+1) + 2)) = 8
tasks = ["A","B","C","D","E","A","B","C","D","E"]
t = 4 # ans = 10
 # ans = max(len(tasks), (max_freq -1 ) * (n +1) + count_of_max_freq)
 # ans = max(10, (2 - 1) * (4 + 1) + 5) = 10

tasks = ["A","A","A", "B","B","B", "C","C","C", "D", "D", "E"]
t = 2 # ans = 12
 # ans = max(12, (2) * (3) + 3) = 12

# B-A-X-B-X-X-B-X-X-B 10

Solution().leastInterval(tasks,t)