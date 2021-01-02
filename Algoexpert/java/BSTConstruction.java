import java.util.*;

class Program {
    static class BST {
        public int value;
        public BST left;
        public BST right;

        public BST(int value) {
            this.value = value;
        }

        public BST insert(int value) {
            // Write your code here.
            // Do not edit the return statement of this method.
            if (this.value > value){
                if (left != null) left.insert(value);
                else left = new BST(value);
            }
            else if (this.value <= value) {
                if (right != null) right.insert(value);
                else right = new BST(value);
            }
            return this;
        }

        public boolean contains(int value) {
            // Write your code here.
            if (this.value == value) return true;
            else if (this.value > value && left != null) return left.contains(value);
            else if (this.value < value && right != null) return right.contains(value);
            return false;
        }

        public BST remove(int value) {
            // Write your code here.
            // Do not edit the return statement of this method.
            removeHelper(null, value);
            return this;
        }

        public BST getSmallest(){
            BST currentNode = this;
            while (currentNode.left != null){
                currentNode = currentNode.left;
            }
            return currentNode;
        }

        public void removeHelper(BST parentNode, int value){
            BST currentNode = this;

            while (currentNode != null){
                if (currentNode.value > value) {
                    parentNode = currentNode;
                    currentNode = currentNode.left;
                }
                else if (currentNode.value < value) {
                    parentNode = currentNode;
                    currentNode = currentNode.right;
                }
                else {
                    if (parentNode == null) {
                        if (currentNode.right != null) {
                            BST nodeToRemove = currentNode.right.getSmallest();
                            currentNode.value = nodeToRemove.value;
                            nodeToRemove.value = value;
                            currentNode.right.removeHelper(currentNode, value);
                        }
                        else if (currentNode.left != null) {
                            currentNode.value = currentNode.left.value;
                            currentNode.right = currentNode.left.right;
                            currentNode.left = currentNode.left.left;
                        }
                        break;
                    }
                    else if (parentNode != null) {
                        if (currentNode.right == null && currentNode.left == null){
                            if (parentNode.left == currentNode) parentNode.left = null;
                            else if (parentNode.right == currentNode) parentNode.right = null;
                        }
                        else if (currentNode.right != null) {
                            BST nodeToRemove = currentNode.right.getSmallest();
                            currentNode.value = nodeToRemove.value;
                            nodeToRemove.value = value;
                            currentNode.right.removeHelper(currentNode,value);
                        }
                        else if (currentNode.left != null) {
                            currentNode.value = currentNode.left.value;
                            currentNode.right = currentNode.left.right;
                            currentNode.left = currentNode.left.left;
                        }
                        break;
                    }
                }
            }
        }
    }
}

    // public static void main(String[] args){
    //     BST john = new BST(1);
    //     int smallest = john.getSmallest();
    //     System.out.println(smallest);
    // }
