# 169. Majority Element (easy)
# TC - O(n^2) and SC - O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = set()
        for n in nums:
            diff.add(n)
        
        majority = 0
        count_track = 0
        for i in diff:
            temp = nums.count(i)

            if count_track < temp:
                majority = i
                count_track = temp

        return majority
