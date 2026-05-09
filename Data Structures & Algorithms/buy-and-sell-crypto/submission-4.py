class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        count = 0

        for price in prices:

            total = price - minPrice
            if price < minPrice:
                minPrice = price
            count = max(count, total)
        return count
            