# 35. Search Insert Position (easy)
# First Solved
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        f = len(nums)

        if 1 == f:
            if nums[0] == target or nums[0] > target:
                return 0
            else:
                return 1

        for i in range(f):
            if nums[i] == target or ():
                return i
        
        for i in range(f):
            if i == 0:
                if target < nums[i]:
                    return 0
                else:
                    continue
            elif nums[i-1] < target < nums[i]:
                return i
        
        return f

# My improved solution
'''
class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) -1
        
        while low <= high:
            mid = (low + high) // 2

            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid

        return low
'''
