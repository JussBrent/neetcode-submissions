class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        count = 0

        for num in numSet:
            #checking if it doesnt have left neighbor
            if num - 1 not in numSet: 
                length = 1
                while (num + length) in numSet:
                    length += 1
                count = max(length, count)
        return count