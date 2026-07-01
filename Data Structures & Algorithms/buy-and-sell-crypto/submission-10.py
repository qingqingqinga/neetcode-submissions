class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        profit = 0
        max_profit = 0

        for i in range(1,len(prices)):
            minprice = min(minprice, prices[i - 1])
            profit = prices[i] - minprice
            max_profit = max(profit, max_profit)
        return max_profit



       