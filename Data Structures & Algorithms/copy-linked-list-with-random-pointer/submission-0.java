/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> copy = new HashMap<>();
        copy.put(null, null);

        Node current = head;

        while (current != null) {
            if (!copy.containsKey(current)) {
                copy.put(current, new Node(0));
            }

            copy.get(current).val = current.val;

            if (!copy.containsKey(current.next)) {
                copy.put(current.next, new Node(0));
            }

            copy.get(current).next = copy.get(current.next);

            if (!copy.containsKey(current.random)) {
                copy.put (current.random, new Node(0));
            }

            copy.get(current).random = copy.get(current.random);

            current = current.next;
        }

        return copy.get(head);
    }
}
