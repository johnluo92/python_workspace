class Solution:
    def scheduleCourse(self, courses):
        
        
        def get_perms(array, permutations, j):
            if j == len(array):
                permutations.append(array[:])

            for i in range(j, len(array)):
                swap(j, i, array)
                get_perms(array, permutations, j+1)
                swap(j, i, array)

        def swap(i,j, array):
            array[i], array[j] = array[j], array[i]
        
        perms = []
        get_perms(courses, perms, 0)
        
        max_count = 0
        
        for perm in perms:
            running_days = 0
            count = 0
            for pair in perm:
                running_days = running_days + pair[0]
                if running_days <= pair[1]:
                    count += 1
                    max_count = max(max_count, count)
                    continue
                else:
                    break
                    
        return max_count        


arr = [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]
print(Solution().scheduleCourse(arr))