class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> st;

        int i = 0;

        while (i < tokens.size()) {
            std::string token = tokens[i];
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();

                if (token == "+") {
                    st.push(b + a);
                } else if (token == "-") {
                    st.push(b - a);
                } else if (token == "*") {
                    st.push(b * a);
                } else if (token == "/") {
                    st.push(b / a);
                }

            } else {
                st.push(std::stoi(token));
            }

            i++;
        }

        return st.top();
    }
};
