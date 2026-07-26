# 55. Jump Game (medium)
# Using Bottom-up Dynamic Programming. Tc- O(n), Sc- O(1)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        goal = l-1

        for i in range(l-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal==0
            
