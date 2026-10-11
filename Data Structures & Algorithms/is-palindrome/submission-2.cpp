class Solution {
public:
    bool isPalindrome(string s) {
       std::string newS = "";

        for (char letter : s) {
            if (isalnum(letter)) {
                newS += std::tolower(letter);
            }
        }

        std::string reversedS = newS;
        std::reverse(reversedS.begin(), reversedS.end());

        return newS == reversedS; 
    }
};
