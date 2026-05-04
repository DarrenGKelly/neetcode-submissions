class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestBuy = prices[0]
        for price in prices[1:]:
            lowestBuy = price if price < lowestBuy else lowestBuy
            newProfit = price - lowestBuy
            maxProfit =  newProfit if newProfit > maxProfit else maxProfit 
        
        return maxProfit