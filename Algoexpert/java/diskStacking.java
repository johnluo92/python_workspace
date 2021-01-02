import java.util.*;

class Solution {

    public static List<Integer[]> diskStacking(List<Integer[]> disks) {
        // Write your code here.
        disks.sort((disk1, disk2) -> disk1[2].compareTo(disk2[2]));

        int[] heights = new int[disks.size()];
        int[] sequence = new int[disks.size()];
        int tallestIdx = 0, tallest = Integer.MIN_VALUE;

        for (int i = 0; i < heights.length; i ++) heights[i] = disks.get(i)[2];
        for (int i = 0; i < heights.length; i ++) sequence[i] = Integer.MIN_VALUE;

        List<Integer[]> stack = new ArrayList<>();

        for (int i = 1; i < disks.size(); i ++){
            var disk2 = disks.get(i);
            for (int j = 0; j < i; j ++){
                var disk1 = disks.get(j);
                if (conditionsSatisfied(disk1, disk2)){
                    int newHeight = heights[j]+disk2[2];
                    if (newHeight > heights[i]){
                        heights[i] = heights[j] + disk2[2];
                        sequence[i] = j;
                    }
                }
                if (heights[i] > tallest){
                    tallest = heights[i];
                    tallestIdx = i;
                }
            }
        }
        System.out.println("tallest is " + tallest + ", tallestIdx " + tallestIdx);

        for (int num : heights) System.out.print(num + " ");
        System.out.println();
        for (int som : sequence) System.out.print(som + " ");
        System.out.println();
        buildSequence(disks, sequence, stack, tallestIdx);
        for (var item : stack) System.out.print(item + " ");
        return stack;
    }

    public static void buildSequence(List<Integer[]> disks, int[] sequence, List<Integer[]> stack, int tallestIdx){
        int curIDx = tallestIdx;
        while (curIDx != Integer.MIN_VALUE){
            var disk = disks.get(curIDx);
            stack.add(0, disk);
            curIDx = sequence[curIDx];
        }
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


        // [      0          1          2          3          4          5]
        // {2, 2, 1}),{2, 1, 2}),{3, 2, 3}),{2, 3, 4}),{4, 4, 5}),{2, 2, 8}
        // [      1          2          5          4          10         8]
        // [      n          n          1          n          2          n]
        System.out.println(Solution.diskStacking(input));
    }
}
