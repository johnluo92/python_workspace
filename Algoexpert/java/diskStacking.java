import java.util.*;

class Solution {

    public static List<Integer[]> diskStacking(List<Integer[]> disks) {
        // Write your code here.
        disks.sort((disk1, disk2) -> disk1[2].compareTo(disk2[2]));

        int[] heights = new int[disks.size()];
        int[] sequence = new int[disks.size()];
        int tallestIdx = Integer.MIN_VALUE;

        for (int i = 0; i < heights.length; i ++) heights[i] = disks.get(i)[2];
        for (int i = 0; i < heights.length; i ++) sequence[i] = Integer.MIN_VALUE;

        List<Integer[]> stack = new ArrayList<>();

        for (int i = 0; i < disks.size()-1; i ++){
            var disk1 = disks.get(i);
            for (int j = i+1; j < disks.size(); j ++){
                var disk2 = disks.get(j);
                if (conditionsSatisfied(disk1, disk2)){
                    int newHeight = disk1[2]+disk2[2];
                    if (newHeight > heights[j]){
                        heights[j] = newHeight;
                        sequence[j] = i;
                    }
                }
            }
        }
        for (var num : heights) System.out.println(num);
        return stack;
    }

    public static boolean conditionsSatisfied(Integer[] disk1, Integer[] disk2){

        if (disk1[0] >= disk2[0] || disk1[1] >= disk2[1] || disk1[2] >= disk2[2]) return false;
        return true;
    }


    public static void main(String[] args){

        List<Integer[]> input = new ArrayList<Integer[]>();
        input.add(new Integer[] {2, 2, 1});
        input.add(new Integer[] {2, 1, 2});
        input.add(new Integer[] {3, 2, 3});
        input.add(new Integer[] {2, 3, 4});
        input.add(new Integer[] {4, 4, 5});
        input.add(new Integer[] {2, 2, 8});
        System.out.println(Solution.diskStacking(input));
    }
}
