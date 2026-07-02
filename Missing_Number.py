# 268. Missing Number (easy)
# My First solution. Tc- O(NlogN), Sc- O(n)
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums)+1 == len(nums):
            return max(nums)+1

        nums.sort()
        for i, v in enumerate(nums):
            if v != i:
                return i


# Better Aternative using formula
# Tc- O(n), Sc- O(1)
'''
class Solution(object):
    def missingNumber(self, nums):
        l = len(nums)
        actual_sum = (l * (l+1)) / 2
        current_sum = sum(nums)

        return actual_sum - current_sum
'''
