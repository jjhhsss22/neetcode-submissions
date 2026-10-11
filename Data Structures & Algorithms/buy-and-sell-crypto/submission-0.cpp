class Solution {
public:
    int maxProfit(vector<int>& prices) {
     
        int min_buy = prices[0];
        int max_profit = 0;
        for (int i = 1; i < prices.size(); i++) {
            min_buy = std::min(min_buy, prices[i]);
            max_profit = std::max(max_profit, prices[i] - min_buy);
        }

        return max_profit;
    }
};
