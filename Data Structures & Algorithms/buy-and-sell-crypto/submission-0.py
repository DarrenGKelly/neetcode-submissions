class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i, price1 in enumerate(prices):
            for j, price2 in enumerate(prices[i+1:]):
                if (price2 - price1 > maxProfit):
                    maxProfit = price2 - price1
        
        return maxProfit