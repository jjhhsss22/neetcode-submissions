class Solution {
public:
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

    int findKthLargest(vector<int>& nums, int k) {
        for (int num : nums) {
            minHeap.push(num);

            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        return minHeap.top();
    }
};
