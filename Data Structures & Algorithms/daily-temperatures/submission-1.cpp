class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> res(temperatures.size(), 0);
        std::stack<int> st;

        for (int i = 0; i < temperatures.size(); i++) {

            while (!st.empty() && temperatures[st.top()] < temperatures[i]) {
                res[st.top()] = i - st.top();
                st.pop();
            }
            
            st.push(i);
        }

        return res;
    }
};
