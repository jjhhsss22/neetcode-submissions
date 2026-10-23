class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_buy = prices[0]
        max_profit = 0

        for i, p in enumerate(prices):
            max_profit = max(max_profit, p - min_buy)
            min_buy = min(min_buy, p)

        return max_profit
