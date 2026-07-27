# 1464. Maximum Product of Two Elements in an Array (easy)
# First solution using sorting. Tc- O(nlogn), Sc- O(1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = nums[-1]
        j = nums[-2]

        return ((i-1) * (j-1))

# Alternate solution using enumerate
# Tc- O(n), Sc- O(1)
class Solution(object):
    def maxProduct(self, nums):
        i = j = 0

        for n in nums:
            if n > i:
                j = i
                i = n
            elif n > j:
                j = n

        return (i-1) * (j-1)
