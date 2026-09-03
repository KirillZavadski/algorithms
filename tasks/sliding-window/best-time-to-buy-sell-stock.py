class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1
        curr = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                curr = prices[sell] - prices[buy]
            if curr > max_profit:
                max_profit = curr
            if prices[sell] < prices[buy]:
                buy += 1
            sell += 1
        return max_profit