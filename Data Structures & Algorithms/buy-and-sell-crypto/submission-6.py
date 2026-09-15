class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            total = price - minPrice
            if price < minPrice:
                minPrice = price
            maxProfit = max(total, maxProfit)
            
        return maxProfit




