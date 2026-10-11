class Solution {
public:
    bool isValid(string s) {
        std::stack<char> st;
        std::unordered_map<char, char> map =
            {{')', '('},
             {'}', '{'},
             {']', '['}};

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (st.empty() || map[c] != st.top()) {
                    return false;
                }
                st.pop();

            }
        }

        return st.empty();
    }
};
