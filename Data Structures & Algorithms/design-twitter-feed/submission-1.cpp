class Twitter {
public:
    std::unordered_map<int, std::unordered_set<int>> follows;
    std::unordered_map<int, std::vector<std::pair<int, int>>> tweets;
    int time;

    Twitter() : time(0) {
    }

    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back({time, tweetId});
        time++;
    }

    std::vector<int> getNewsFeed(int userId) {
        std::vector<int> newsFeed;
        std::priority_queue<std::pair<int,int>, std::vector<std::pair<int,int>>, std::greater<>> minHeap;

        follows[userId].insert(userId);

        for (int followeeId : follows[userId]) {
            for (auto& tweet : tweets[followeeId]) {
                minHeap.push(tweet);

                if (minHeap.size() > 10) {
                    minHeap.pop();
                }
            }
        }

        while (!minHeap.empty()) {
            newsFeed.push_back(minHeap.top().second);
            minHeap.pop();
        }

        std::reverse(newsFeed.begin(), newsFeed.end());
        return newsFeed;
    }

    void follow(int followerId, int followeeId) {
        follows[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        if (follows[followerId].count(followeeId)) {
            follows[followerId].erase(followeeId);
        }
    }
};