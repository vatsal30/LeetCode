class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        left = 0
        right = m
        while left < right:
            mid = left + (right-left) // 2
            if matrix[mid][n] >= target:
                right = mid
            else:
                left = mid + 1
        m = left
        left = 0
        right = n
        while left <= right:
            mid = left + (right-left) // 2
            if matrix[m][mid] == target:
                return True
            if matrix[m][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False