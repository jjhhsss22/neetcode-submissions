class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        target_row = self.searchRow(matrix, target)
        
        if not target_row:
            return False

        left = 0
        right = len(target_row) - 1

        while left <= right:
            mid = (left + right) // 2

            if target_row[mid] == target:
                return True
            elif target_row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

    def searchRow(self, matrix, target):
        left_row = 0
        right_row = len(matrix) - 1

        while left_row <= right_row:
            mid_row = (left_row + right_row) // 2

            if matrix[mid_row][0] > target:
                right_row = mid_row - 1
            elif matrix[mid_row][-1] < target:
                left_row = mid_row + 1
            else:
                return matrix[mid_row]

        return None