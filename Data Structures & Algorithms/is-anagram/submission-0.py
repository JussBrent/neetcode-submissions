class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashmap = {}
        hashmap2 = {}

        for ch in s:
            if ch in hashmap:
                hashmap[ch] +=1 
            else:
                hashmap[ch] = 1

        for c in t:
            if c in hashmap2:
                hashmap2[c] +=1 
            else:
                hashmap2[c] = 1

        if hashmap == hashmap2:
            return True
        else:
            return False

        

            
