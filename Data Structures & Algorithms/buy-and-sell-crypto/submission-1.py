class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxprofit = 0

        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                maxprofit= max(maxprofit,profit)
        return maxprofit