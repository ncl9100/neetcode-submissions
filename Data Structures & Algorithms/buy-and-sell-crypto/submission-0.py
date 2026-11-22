class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = max(prices)
        for i in range(1, len(prices)):
            buy = min(buy, prices[i-1])
            max_profit = max(max_profit, prices[i] - buy)
        return max_profit

            


        