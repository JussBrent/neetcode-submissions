class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            profit = price - minPrice
            if price < minPrice:
                minPrice = price
            maxProfit = max(maxProfit, profit)

        return maxProfit 