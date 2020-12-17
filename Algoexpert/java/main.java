public class main{
    
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
