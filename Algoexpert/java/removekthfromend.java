import java.util.*;

class Program {
  public static void removeKthNodeFromEnd(LinkedList head, int k) {
    // Write your code here.
        int counter = 0, length = 1;
        
        LinkedList prev = null, node = head, cur = head.next;
        
        while (node.next != null){
            prev = node;
            node = node.next;
            length ++;
        }
        if (length - k == 0){
            head.value = head.next.value;
            head.next = head.next.next;
            return;
        }
        if (k == 1){
            System.out.println(prev.value);
            prev.next = null;
            System.out.println(head.value);
            return;
        }
        
        prev = head;
        while (counter != length-k){
            counter ++;
            prev = cur;
            cur = cur.next;
        }
        prev.value = prev.next.value;
        prev.next = cur.next;
        
  }

  static class LinkedList {
    int value;
    LinkedList next = null;

    public LinkedList(int value) {
      this.value = value;
    }
  }
}
