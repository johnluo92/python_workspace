import java.util.*;

class Program {
  public static List<Integer> riverSizes(int[][] grid) {
    boolean[][] traversed = new boolean [grid.length][grid[0].length]; 

    System.out.println(traversed[0].length);
    System.out.println(traversed.length);

    List<Integer> answer = new ArrayList<Integer>();

    for (int i = 0; i < traversed.length; i++) 
      for (int j = 0; j < traversed[i].length; j++){
        System.out.println("traversed[" + i + "][" + j + "] = "+ traversed[i][j]);
        if (!traversed[i][j]){
          traversed[i][j] = true;
          countIslands(grid, traversed, i, j, answer);
        }
      }
      return answer;
    }

    public static void countIslands(int[][] grid, boolean[][] traversed, int i, int j, List<Integer> answer){
      int currentIslands = 0;
      
      Stack<Integer[]> stack = new Stack<Integer[]>();
      stack.push(new Integer[] {i, j});
      
      while(!stack.empty()){

        Integer[] new_cord = stack.pop();
        i = new_cord[0];
        j = new_cord[1];
        
        if (grid[i][j] == 1){
          getNeighbors(i, j, grid, traversed, stack);
          currentIslands ++;
        }
      }
      if (currentIslands > 0)
        answer.add(currentIslands);
    }

    public static void getNeighbors(int i, int j, int[][] grid, boolean[][] traversed, Stack<Integer[]> stack){
      int[][] coords = {{0,-1}, {-1,0}, {0,1}, {1, 0}};
      
      for (int[] coord : coords){
        int new_x = i + coord[0];
        int new_y = j + coord[1];
        
        if (new_x >=0 && new_x < grid.length && new_y >= 0 && new_y < grid[0].length){
          if (!traversed[new_x][new_y]){
            traversed[new_x][new_y] = true;
            stack.push(new Integer[] {new_x, new_y});
          }
        } 
      }
    }

    public static void main(String[] args){

      int [][] grid = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'}
      };
      Program sol = new Program();
      var answer = sol.riverSizes(grid);
      System.out.println(answer);
    }
  }