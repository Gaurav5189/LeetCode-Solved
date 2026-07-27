# 45. Jump Game II (medium)
# Used recursion. Tc- O(n^2), Sc- O(n^2) or O(n) auxiliary space
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0]

        def jump_count(combination):
            l = len(combination)
            goal = l-1

            if l == 1:
                return count[0]

            for i in range(0, l-1):
                if i + combination[i] >= goal:
                    count[0] += 1
                    jump_count(combination[0:i+1])
                    break

        jump_count(nums)
        return count[0]

# Alternative solution using greedy method
# Tc- O(n), Sc- O(1)
class Solution(object):
    def jump(self, nums):
        jumps = current_index = farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])

            if i == current_index:
                jumps += 1
                current_index = farthest

        return jumps
