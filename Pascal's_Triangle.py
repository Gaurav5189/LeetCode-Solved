# 118. Pascal's Triangle (easy)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri_list = []

        for i in range(numRows):
            row = [1] * (i+1)

            for j in range(1, i):
                row[j] = tri_list[i-1][j-1] + tri_list[i-1][j]
                
            tri_list.append(row)

        return tri_list
