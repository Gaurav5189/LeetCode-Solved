# 15. 3Sum (medium)
# Using Two pointer. TC - O(n^2), SC - O(logN)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        result = []

        for i in range(l-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = l - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if current == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and (nums[left] == nums[left - 1]):
                        left += 1

                    while left < right and (nums[right] == nums[right + 1]):
                        right -= 1

                elif current < 0:
                    left += 1
                else:
                    right -= 1
            
        return result
