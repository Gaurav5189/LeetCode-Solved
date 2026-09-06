# 162. Find Peak Element (medium)
# Tc- O(logn), Sc- 0(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid+1
            else:
                right = mid

        return left
