class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        #same as robber house 1 but you're checking for edge cases
        #skipping the first house and last house; also checking if only one house

    def helper(self,nums):
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