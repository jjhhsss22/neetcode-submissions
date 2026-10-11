class Solution {
public:
    std::priority_queue<std::pair<int, int>> heap;

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        for (int i = 0; i < points.size(); i++) {
            int x = points[i][0];
            int y = points[i][1];
            int distance = x * x + y * y;

            heap.push({distance, i});

            if (heap.size() > k) {
                heap.pop();
            }
        }

        std::vector<std::vector<int>> res;

        while (!heap.empty()) {
            res.push_back({points[heap.top().second][0], points[heap.top().second][1]});
            heap.pop();
        }

        return res;
    }
};
