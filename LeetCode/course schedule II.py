#course schedule II

class Solution:
    def findOrder(self, numCourses, prerequisites): # == > list
        # numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        my_keys = {}
        for pairs in prerequisites:
            key = pairs[1]
            if key not in my_keys:
                my_keys[key] = [pairs[0]]
            else:
                my_keys[key].append(pairs[0])

        visisted = [0 for _ in range(numCourses)]
        ans = {}
        cycle = False

        print(my_keys)

        for prereq in my_keys:
            if self.is_acyclical(prereq, my_keys, visisted, ans):
                if prereq not in ans:
                    ans[prereq] = None
                continue
            else:
                cycle = True
                break
        if len(ans) < numCourses:
            self.find_missing(ans, numCourses)

        ans = [pairs[0] for pairs in reversed(ans.items())]

        return ans if cycle is False else []
        
    def is_acyclical(self, key, my_keys, visisted, ans): # ==> boolean
        if visisted[key] == -1:
            return False

        if visisted[key] == 1:
            return True

        visisted[key] = -1

        if key in my_keys:
            for depend in my_keys[key]:
                if self.is_acyclical(depend, my_keys, visisted, ans):
                    if depend not in ans:
                        ans[depend] = None
                else:
                    return False

        visisted[key] = 1

        return True

    def find_missing(self, ans, numCourses):
        to_append = []
        for i in range(numCourses):
            if i not in ans:
                ans[i] = None

nums = 4
reqs = [[2,1],[3,1],[2,3],[1,0]]

nums = 4
reqs = [[2,1],[3,1],[2,3],[1,0],[0,1]]

nums = 3
reqs = [[1,0]]
print(Solution().findOrder(nums, reqs))


'''
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
'''