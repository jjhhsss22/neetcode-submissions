class KthLargest {
public:
    int k;
    std::priority_queue<int, vector<int>, greater<int>> minHeap;

    KthLargest(int k, std::vector<int>& nums) {
        this->k = k;

        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
    }

    int add(int val) {
        minHeap.push(val);
        if (minHeap.size() > k) {
            minHeap.pop();
        }

        return minHeap.top();
    }
};
