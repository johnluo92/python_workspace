import java.util.*;


import java.util.*;

class Solution {
  // Tip: You can use `element instanceof ArrayList` to check whether an item
  // is an array or an integer.
  public static int productSum(List<Object> array) {
    // Write your code here.
    int total = 0;
    for (var obj : array){
      if (obj instanceof ArrayList)
          total += multiplyLevel(2, (ArrayList<Object>) obj);
      else
        total += (int)obj;
    }
    return total;
  }
  
  public static int multiplyLevel(int level, List<Object> array){
    int total = 0;
    for (var obj : array){
      if (obj instanceof ArrayList){
          total += multiplyLevel(level+1, (ArrayList<Object>) obj);
      }
      else
        total += (int) obj;
    }
    return level * total;
  }

      public static void main(String[] args){

    List<Object> test =
        new ArrayList<Object>(
            Arrays.asList(
                5,
                2,
                new ArrayList<Object>(Arrays.asList(7, -1)),
                3,
                new ArrayList<Object>(
                    Arrays.asList(6, new ArrayList<Object>(Arrays.asList(-13, 8)), 4))));
      System.out.println(Solution.productSum(test));
    }
}