class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #have an index running through then your lo and high
        #sort it out first
        nums.sort()
        res = []
        # -4 -1 -1 0 1 2
        for i in range(len(nums)):
            
            lo = i + 1
            high = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while lo < high:
                total = nums[i] + nums[lo] + nums[high]

                if total > 0:
                    high -= 1

                elif total < 0:
                    lo += 1
                    
                elif total == 0:
                    res.append([nums[i], nums[lo], nums[high]])

                    while lo < high and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < high and nums[high] == nums[high - 1]:
                        high -= 1
                        
                    lo += 1
                    high -= 1
                    
        return res
                

        
