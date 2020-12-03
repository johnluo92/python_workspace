import sys

class Solution:
    def minPathSum(self, grid):

        min_map = [[False for col in row] for row in grid]
        min_map[0][0] = grid[0][0]

        self.fill_map(grid, min_map)

        # for row in min_map:
        #     print(row)

        print(min_map[-1][-1])
        return min_map[-1][-1]

    def fill_map(self, grid, min_map):

        queue = [(0,0)]
        while len(queue):
            i, j = queue.pop(0)
            # print(i,j)
            self.get_neighbors(min_map, queue, i, j)
            if i != 0 or j != 0: # if both i and j are 0 then we are at the start
                self.get_shortest_path(grid, min_map, i, j)

            # for row in min_map:
            #     print(row)
            # print(queue)
            # print()
            
        #when no more neighbors can be found we've reached the end
        return

    def get_neighbors(self, min_map, queue, i, j):
        for x,y in ((1, 0), (0, 1)):
            if i+x < len(min_map) and j+y < len(min_map[0]):
                if min_map[i+x][j+y] is False:
                    queue.append((i+x,j+y))
                    min_map[i+x][j+y] = True

    def get_shortest_path(self, grid, min_map, i, j):
        origin = []
        for x,y in ((-1, 0), (0, -1)):
            if i+x >= 0 and j+y >= 0:
                origin.append(min_map[i+x][j+y])
        min_map[i][j] = grid[i][j] + min(origin)


grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]

        # [1,n,n]
        # [n,n,n]
        # [n,n,n]

grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
        [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
        [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
        [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
        [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
        [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
        [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
        [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
        [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
        [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
        [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
        [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
grid = [[1,3,1],
        [1,5,1],
        [1,8,1]]

grid = [[7,8,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
        [16,13,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
        [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
        [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
        [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
        [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

Solution().minPathSum(grid)