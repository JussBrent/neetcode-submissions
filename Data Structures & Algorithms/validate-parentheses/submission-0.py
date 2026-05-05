class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        combine = {")" : "(", "}" : "{", "]" : "["}

        for ch in s:
            if ch in combine:
                if stack and stack[-1] == combine[ch]:
                    stack.pop()
                else:
                    return False
            else:
              stack.append(ch)
        return not stack
                


        