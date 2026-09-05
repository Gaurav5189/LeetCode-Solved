# 74. Search a 2D Matrix  (medium)
# Tc- O(log(n+m)), Sc- O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows*cols - 1
        
        while high >= low:
            mid = low + (high - low) // 2

            row = mid // cols
            col = mid % cols
            value = matrix[row][col]

            if value == target:
                return True
            elif value >= target:
                high = mid-1
            else:
                low = mid+1

        return False
