# 1260. Shift 2D Grid (easy)
# converting 2D list to 1D and slice & shift. Tc and Sc - O(n)
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        result = []

        grid_list = [v for row in grid for v in row]

        k = k%len(grid_list)
        
        if k != 0:
            grid_list = grid_list[-k:] + grid_list[:-k]

        for i in range(rows):
            row = grid_list[i*cols : (i+1)*cols]
            result.append(row)

        return result
