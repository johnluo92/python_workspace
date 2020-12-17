import java.util.*;

class Solution {
    public int numIslands(char[][] grid) {
        boolean[][] traversed = new boolean [grid.length][grid[0].length]; 
      
        System.out.println(traversed[0].length);
        System.out.println(traversed.length);
      
        List<Integer> answer = new ArrayList<>();
      
        for (int i = 0; i < traversed.length; i++) 
            for (int j = 0; j < traversed[i].length; j++){
                System.out.println("traversed[" + i + "][" + j + "] = "+ traversed[i][j]);
                if (traversed[i][j] != true){
                  traversed[i][j] = true;
                  if (grid[i][j] != 0)
                    countIslands(grid, traversed, i, j, answer);
                }
            }
      
        return answer;
    }
  
  
    public void countIslands(char[][] grid, boolean[][] traversed, int i, int j, List<Integer> answer){
      int[][] coords = {{0,-1}, {-1,0}, {0,1}, {1, 0}};
      
      List
    }
  
      public static void main(String[] args){

      char [][] grid = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'}
      };
      Solution sol = new Solution();
      var answer = sol.numIslands(grid);
      System.out.println(answer);
    }
}