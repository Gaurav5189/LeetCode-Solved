# 136. Single Number (easy)
# my first solution tc - O(n), sc - O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)

        return next(iter(seen))


# Alternative tc - O(n), sc - O(1)
'''
class Solution(object):
    def singleNumber(self, nums):

        seen = 0
        for num in nums:
            seen = seen ^ num

        return seen
'''
