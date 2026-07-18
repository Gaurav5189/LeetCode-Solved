# 1979. Find Greatest Common Divisor of Array (easy)
# Tc- O(n+log(max(nums))),Sc- O(n)
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = min(nums)
        l = max(nums)

        if s==l:
            return l
        
        while s:
            l, s = s, l%s

        return l
