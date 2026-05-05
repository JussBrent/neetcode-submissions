class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(index, path):
            #base case
            if index == len(nums):
                res.append(path[:]) #making a copy
                return
                                
            #make choice
            #decision 1 to include nums[index]
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            #skip nums
            backtrack(index + 1, path)

        backtrack(0,[])
        return res

        
