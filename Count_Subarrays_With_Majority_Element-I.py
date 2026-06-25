# 3737. Count Subarrays With Majority Element I (medium)
# o(n^2) brute force
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = 0
        n = len(nums)

        for i in range(n):
            c_sum = 0

            for j in range(i, n):
                c_sum+=1 if nums[j] == target else -1

                total+=1 if c_sum > 0 else 0

        return total
