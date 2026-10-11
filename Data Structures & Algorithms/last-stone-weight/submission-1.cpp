class Solution {
public:
    std::priority_queue<int> heap;

    int lastStoneWeight(std::vector<int>& stones) {
        this->heap = std::priority_queue(stones.begin(), stones.end());

        while (this->heap.size() > 1) {
            int stone1 = this->heap.top();
            this->heap.pop();
            int stone2 = this->heap.top();
            this->heap.pop();

            if (stone1 != stone2) {
                this->heap.push(abs(stone1 - stone2));
            }

        }

        return this->heap.empty() ? 0 : this->heap.top();
    }
};
