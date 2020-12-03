class Solution:
    def minPathSum(self, grid):
        min_map = [[float('inf') for col in row] for row in grid]
        
        self.path_sum = float('inf')
        
        self.get_min_path(grid, min_map, 0, 0, 0)
        for row in min_map:
            print(row)
        

        print('\nmin_path is: ', self.path_sum)
        return self.path_sum
    
    def get_min_path(self, grid, min_map, i, j, curr):
        # print(f'currently at {i},{j}')
        # for row in min_map:
        #     print(row)
        # print()
        
        curr += grid[i][j]
        
        if curr < min_map[i][j]:
            min_map[i][j] = curr
        else:
            return
        
        if i == len(grid)-1 and j == len(grid[0])-1:
            # print('finished')
            self.path_sum = min(self.path_sum, curr)
            return
        

        # go right col by col
        if j + 1 < len(grid[0]):
            self.get_min_path(grid, min_map, i, j + 1, curr)        
        # go down row by row
        if i + 1 < len(grid):
            self.get_min_path(grid, min_map, i + 1, j, curr)


grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]

grid =[
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]

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

grid1 = [[1,3,1],
        [1,5,1],
        [1,8,1]]

grid1 = [[7,8,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
        [16,13,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
        [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
        [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
        [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
        [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

Solution().minPathSum(grid1)
