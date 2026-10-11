class TimeMap {
public:
    std::unordered_map<std::string, std::vector<std::pair<std::string, int>>> map;

    TimeMap() {
    }

    void set(std::string key, std::string value, int timestamp) {
        map[key].push_back({value, timestamp});
    }

    std::string get(std::string key, int timestamp) {
        if (!map.count(key)) return "";

        int l = 0;
        int r = map[key].size() - 1;
        
        std::string recent = "";

        while (l <= r) {
            int m = (l + r) / 2;

            if (map[key][m].second <= timestamp) {
                recent = map[key][m].first;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return recent;

    }
};
