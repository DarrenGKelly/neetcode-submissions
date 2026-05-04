class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestBuy = prices[0]
        for price in prices[1:]:
            lowestBuy = min(lowestBuy, price)
            maxProfit =  max(maxProfit, price - lowestBuy)
        
        return maxProfit