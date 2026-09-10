class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:

            width = r - l
            area = (min([heights[l], heights[r]]) * width)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
            
            res = max(area, res)
            
        return res



            