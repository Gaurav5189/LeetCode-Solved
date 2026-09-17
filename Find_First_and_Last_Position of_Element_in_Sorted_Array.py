# 34. Find First and Last Position of Element in Sorted Array (medium)
# using binary search. Tc-(logn), Sc-O(1)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findIndex(isFirst):
            left = 0
            right = len(nums) - 1
            found = -1

            while left <= right:
                mid = (left+right) // 2

                if nums[mid] == target:
                    found = mid
                    if isFirst:
                        right = mid - 1     # to binary search left again
                    else:
                        left = mid + 1      # to binary search right again

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return found

        return [findIndex(True), findIndex(False)]
