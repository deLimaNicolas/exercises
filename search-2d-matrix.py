from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        selectedRow = None
        left, right = 0, ROWS - 1

        while left <= right:
            midRow = left + (right - left) // 2
            if matrix[midRow][-1] == target:
                return True
            if matrix[midRow][0] == target:
                return True
            if target < matrix[midRow][-1] and target > matrix[midRow][0]:
                selectedRow = midRow
            if matrix[midRow][-1] < target:
                left = midRow + 1
            elif matrix[midRow][-1] > target:
                right = midRow -1

        if not selectedRow != None:
            return False

        left, right = 0, COLS - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[selectedRow][mid] == target:
                return True
            elif matrix[selectedRow][mid] > target:
                right = mid - 1

            elif matrix[selectedRow][mid] < target:
                left = mid + 1

        return False
