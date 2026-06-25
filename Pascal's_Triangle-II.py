# 119. Pascal's Triangle II (easy)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = []

        for i in range(rowIndex+1):
            temp_row = [1] * (i+1)
            
            for j in range(1, i):
                temp_row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(temp_row)

        return triangle[-1]


# alternative O(n) solution using formula => C(k, i) = [previous no]C(k, i-1) x (k - i + 1)/i
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        current = 1

        for i in range(1, rowIndex+1):
            current = current * (rowIndex - i +1) // i

            row.append(current)

        return row
'''
