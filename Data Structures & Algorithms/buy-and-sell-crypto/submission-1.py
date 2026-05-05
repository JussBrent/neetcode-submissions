class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxPrice = 0

        for price in prices:
            if price < minPrice:
                minPrice = price    
            total = price - minPrice

            if total > maxPrice:
                maxPrice = total
            
        return maxPrice