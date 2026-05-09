class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        hash = set()
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        
