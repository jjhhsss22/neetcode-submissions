class Solution {
public:
    int findDuplicate(vector<int>& nums) {

        // this is Floyd's Cycle Detection algorithm (Turtoise & Hare algorithm)
        // fast pointer travels two nodes at a time
        // slow pointer travels one at a time
        //  when they meet, 
        // the distance between that node and the starting node of the cycle
        // is equal to the distance from the start to the cycle node
        // so create another slow pointer from the head and traverse with both pointers
        // until they meet to find the repeating node.

        int fast = 0, slow = 0;

        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];

            if (slow == fast) {
                break;
            }
        }

        int slow2 = 0;

        while (true) {
            slow = nums[slow];
            slow2 = nums[slow2];

            if (slow == slow2) {
                break;
            }
        }

        return slow;
    }
};
