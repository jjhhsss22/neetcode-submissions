class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;

        std::vector<int> s1count(26, 0), s2count(26, 0);
        int matches = 0;


        for (int i = 0; i < s1.length(); i++) {
            s1count[s1[i] - 'a']++;
            s2count[s2[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (s1count[i] == s2count[i]) {
                matches++;
            }
        }

        if (matches == 26) return true;

        int l = 0;
        for (int r = s1.length(); r < s2.length(); r++) {

            s2count[s2[r] - 'a']++;
            if (s2count[s2[r] - 'a'] == s1count[s2[r] - 'a']) {
                matches++;
            } else if (s2count[s2[r] - 'a'] - 1 == s1count[s2[r] - 'a']) {
                matches--;
            }

            s2count[s2[l] - 'a']--;
            if (s2count[s2[l] - 'a'] == s1count[s2[l] - 'a']) {
                matches++;
            } else if (s2count[s2[l] - 'a'] + 1 == s1count[s2[l] - 'a']) {
                matches--;
            }

            l++;

            if (matches == 26) return true;

        }

        return false;

    }
};
