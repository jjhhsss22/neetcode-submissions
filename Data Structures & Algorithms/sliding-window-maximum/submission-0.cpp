class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        std::deque<int> dq;
        std::vector<int> result;

        int l = 0;

        for (int r = 0; r < nums.size(); r++) {
            while (!dq.empty() && nums[r] > nums[dq.back()]) {
                dq.pop_back();
            }

            dq.push_back(r);

            if (r >= k) {
                l++;
            }

            while (!dq.empty() && l > dq.front()) {
                dq.pop_front();
            }

            if (r + 1 >= k) {
                result.push_back(nums[dq.front()]);
            }

        }
        return result;
    }
};
