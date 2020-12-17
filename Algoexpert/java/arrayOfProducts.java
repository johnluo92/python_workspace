import java.util.*;

class Solution {
  public int[] arrayOfProducts(int[] array) {
    // Write your code here.
    var arrayLen = array.length;
    int[] leftToRight = new int[arrayLen];
    leftToRight[0] = 1;
    var runningProduct = 1 * array[0];
    for (int i = 1; i < arrayLen; i ++){
      leftToRight[i] = runningProduct;
      runningProduct = runningProduct * array[i];
    }
    int[] rightToLeft = new int[array.length];
    rightToLeft[arrayLen-1] = 1;
    runningProduct = 1 * array[arrayLen-1];
    for (int i = arrayLen-2; i >= 0; i --){
      rightToLeft[i] = runningProduct;
      runningProduct = runningProduct * array[i];
    }
    int[] ans = new int[arrayLen];
    for (int i = 0; i < arrayLen; i ++){
      ans[i] = leftToRight[i] * rightToLeft[i];
    }
    
    for (int num : ans){
      System.out.println(num);
    }
    return ans;
  }
  
      public static void main(String[] args){

      int[] array = {1,2,3,4,0};
      Solution sol = new Solution();
      var answer = sol.arrayOfProducts(array);
      System.out.println(answer);
    }
}