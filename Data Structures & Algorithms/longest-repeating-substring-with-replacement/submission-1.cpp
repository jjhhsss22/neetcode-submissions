class Solution {
public:
    int characterReplacement(string s, int k) {
        if (s.empty()) return 0;

        std::unordered_map<char, int> hashMap;

        int l = 0;
        int max = 0;
        int result = 0;

        for (int r = 0; r < s.length(); r++) {
            hashMap[s[r]]++;

            max = std::max(max, hashMap[s[r]]);

            while (r - l - max + 1 > k) {
                hashMap[s[l]]--;
                l++;
            }

            result = std::max(result, r - l + 1);
        }

        return result;
    }
};
