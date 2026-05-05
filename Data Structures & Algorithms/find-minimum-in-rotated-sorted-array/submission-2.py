class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            #when L overlaps, the loops end. thats why you return nums[l]
            mid = (l+r) // 2

            if nums[mid] <= nums[r]:
                r = mid #blueprint is here, you are shrinking the array
            else:
                l = mid + 1
        return nums[l]
                