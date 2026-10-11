class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) return "";
        if (s.size() < t.size()) return "";

        if (s == t) return t;

        std::unordered_map<char, int> mapT;
        std::unordered_map<char, int> mapS;

        int l = 0;
        int minL = 0;
        int minLEN = INT_MAX;

        for (char c : t) {
            mapT[c]++;
        }

        int matches = 0;
        int required = mapT.size();

        for (int r = 0; r < s.size(); r++) {
            char c = s[r];
            mapS[c]++;

            if (mapS[c] == mapT[c]) {
                matches++;
            }

            while (matches == required) {
                if (r - l + 1 < minLEN) {
                    minLEN = r - l + 1;
                    minL = std::max(minL, l);
                }

                char leftC = s[l];
                mapS[leftC]--;

                if (mapT.count(leftC) && mapS[leftC] < mapT[leftC]) {
                    matches--;
                }

                l++;
            }

        }

        return (minLEN == INT_MAX) ? "" : s.substr(minL, minLEN);
    }
};
