def diskStacking(disks):
    # Write your code here.
#     [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
    
#   [[1, 3, 1], [2, 1, 2], [3, 2, 3], [2, 3, 4], [4, 4, 5], [2, 2, 8]]
#   ans = [[2,1,2], [3,2,3], [4,4,5]]
    
    disks.sort(key = lambda x: x[2])

    heights = [disk[2] for disk in disks] # disk[2] being the height of every disk
    sequences = [None for _ in disks]
    
    maxheight = -float('inf')
    max_height_idx = 0
# SEQUENCES = [    0,         1,         2,         3,         4,         5,]
# SEQUENCES = [  NONE,       NONE,      NONE,      NONE,     NONE,      NONE,]
    #         [[1, 3, 1], [2, 1, 2], [3, 2, 3], [2, 3, 4], [4, 4, 5], [2, 2, 8]]
# heights = [         1,         2          3          4          5          8]
# heights = [         1,         2          5          4          10         8]
# SEQUENCES = [  NONE,       NONE,       1,       NONE,        2,      NONE,]
    
    for i in range(1, len(disks)):
        disk2 = disks[i]
        for j in range(0, i):
            disk1 = disks[j]
            if validate_dimensions(disk1, disk2):
                if heights[j] + disk2[2] > heights[i]:
                    heights[i] = heights[j] + disk2[2]
                    sequences[i] = j
            if heights[i] > maxheight:
                maxheight = max(maxheight, heights[i])
                max_height_idx = max(max_height_idx, i)
                
    print(max_height_idx)
                
    ans = build_sequence(disks, sequences, max_height_idx)
    print(ans)
    return ans
                    
def validate_dimensions(d1, d2):
    return d1[0] < d2[0] and d1[1] < d2[1] and d1[2] < d2[2]

def build_sequence(disks, sequences, curr_id):
    sequence = []
    while curr_id is not None:
        disk = disks[curr_id]
        print(disk)
        sequence.append(disk)
        curr_id = sequences[curr_id]
        
    return list(reversed(sequence))
                    
                    
                    