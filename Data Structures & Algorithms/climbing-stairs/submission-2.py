class Solution:
    def climbStairs(self, n: int) -> int:
        
        one , two = 1, 1

        for i in range(n -1):
            temp = one
            one = one + two #update one before the shift
            two = temp #shift two to previous value of one
        return one #once loop is finished return what one lands on