class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
         std::unordered_map<std::string, std::vector<std::string>> map;

        for (int i = 0; i < strs.size(); i++) {
            std::vector temp(26, 0);

            std::string s = strs[i];

            for (char c : s) {
                temp[c - 'a']++;
            }

            std::string key = "";

            for (int j = 0; j < 26; j++) {
                key += temp[j];
            }

            map[key].push_back(s);

        }

        std::vector<std::vector<std::string>> ans;
            
        for (const auto& [key, value] : map) {
            ans.push_back(value);
        }

        return ans;    
    }
};
