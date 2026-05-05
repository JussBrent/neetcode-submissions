class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hash = set(nums)

        longest = 0

        for n in nums:
            if (n-1) not in hash:
                length = 0
                while (n + length) in hash:
                    length += 1
                longest = max(length, longest)
        return longest                
