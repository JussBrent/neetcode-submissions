class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] *  n
        #return base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n): # 2 inclusive and n -1 inclusive
            dp[i] = max(dp[i- 2] + nums[i], dp[i-1])
            #first in parenthesis is what you get if you rob
            #second is keeping what you got from what you robbed before
        
        return dp[n -1]