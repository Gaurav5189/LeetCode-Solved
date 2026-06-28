# 217. Contains Duplicate (easy)
# TC - O(n) & SC - O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dist = set(nums)

        return False if len(nums) == len(dist) else True


# the last line can also be -
# return len(nums) != len(dist)
