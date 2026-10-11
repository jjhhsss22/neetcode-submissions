class Solution {
public:
    int leastInterval(std::vector<char>& tasks, int n) {
        std::vector count(26, 0);
        for (char task : tasks) {
            count[task - 'A']++;
        }

        std::priority_queue<int> maxHeap;

        for (int num : count) {
            if (num > 0) {
                maxHeap.push(num);
            }
        }

        int time = 0;
        std::queue<std::pair<int, int>> q;
        while (!maxHeap.empty() || !q.empty()) {
            time++;

            if (!q.empty() && q.front().second == time) {
                maxHeap.push(q.front().first);
                q.pop();
            }

            if (!maxHeap.empty()) {
                int task = maxHeap.top() - 1;
                maxHeap.pop();

                if (task > 0) {
                    q.push({task, time + n + 1});
                }
            }
        }
        return time;
    }
};
