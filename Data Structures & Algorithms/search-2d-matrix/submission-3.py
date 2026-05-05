class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        columns = len(matrix[0])

        l = 0
        r = rows * columns - 1

        while l <= r:
            mid = (l + r) // 2

            num = matrix[mid // columns][mid % columns]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            elif num > target:
                r = mid - 1
        return False


