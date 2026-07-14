class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return None

        water = 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            #once you find a number bigger you add the smaller number and continue
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]
        
        return water