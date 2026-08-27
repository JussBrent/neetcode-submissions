class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        solve = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in solve:
                return [solve[diff],i]
            solve[num] = i
            
                