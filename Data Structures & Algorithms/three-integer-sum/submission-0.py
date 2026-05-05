class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            #i greater than 0 means its not the first value
            # a is seeing if its the same value
            if i > 0 and a == nums[i - 1]:
                continue
            
            #i + 1 is preventing the use of the same index
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    #you dont want same sum so you update pointer
                    # you dont want left to pass r
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
