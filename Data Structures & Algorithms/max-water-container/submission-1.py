class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #tricky part is just computing the area

        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            #width * height 
            #width (r - l)
            #height is getting the minimum height so water dont spill out
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area) 

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res