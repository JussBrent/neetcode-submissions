class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s1 = {}
        t1 = {}

        for i in range(len(s)):
            s1[s[i]] = 1 + s1.get(s[i], 1)
            t1[t[i]] = 1 + t1.get(t[i], 1)

        return s1 == t1

