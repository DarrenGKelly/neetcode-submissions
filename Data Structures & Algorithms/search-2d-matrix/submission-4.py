class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0

        # Binary Search Rows
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2

            if (matrix[mid][0] <= target and matrix[mid][-1] >= target):
                row = mid
                break
            elif (matrix[mid][0] < target):
                low = mid + 1
            else:
                high = mid - 1

        
        # Binary Search Columns
        low, high = 0, len(matrix[mid]) - 1
        while low <= high:
            mid = (low + high) // 2
            if (matrix[row][mid] == target):
                return True
            elif (matrix[row][mid] < target):
                low = mid + 1
            else:
                high = mid - 1

        return False