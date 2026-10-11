class Solution {
public:
    std::priority_queue<int> maxHeap;

    int findKthLargest(vector<int>& nums, int k) {
        for (int num : nums) {
            maxHeap.push(num);

            if (maxHeap.size() > nums.size() - k + 1) {
                maxHeap.pop();
            }
        }

        return maxHeap.empty() ? 0 : maxHeap.top();
    }
};
