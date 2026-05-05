class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i, num in enumerate(nums):

            station = target - num

            if station in hashmap:
                return [hashmap[station], i]
            hashmap[num] = i


