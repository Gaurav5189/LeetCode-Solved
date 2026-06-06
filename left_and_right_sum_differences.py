# 2574. Left and Right Sum Differences (easy level)
# My original solution
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if 1 == len(nums):
            return [0]
        
        l_sum = []
        r_sum = []

        if 0 == len(l_sum):
            l_sum.append(0)
        for i in range(0, len(nums)-1):
            if 0 == i:
                a = nums[i]
                l_sum.append(a)
            else:
                a = nums[i] + l_sum[i]
                l_sum.append(a)
        
        if 0 == len(r_sum):
            r_sum.append(0)
        for i in range(len(nums)-1, 0, -1):
            if i == len(nums)-1:
                a = nums[i]
                r_sum.insert(0, a)
            else:
                a = nums[i] + r_sum[0]
                r_sum.insert(0, a)
        
        for i in range(len(nums)):
            nums[i] = l_sum[i] - r_sum[i]
            nums[i] = abs(nums[i])

        return nums


# Better alternative
'''
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)
        left = 0
        ans = []

        for num in nums:
            right = total - left - num
            ans.append(abs(left - right))
            left += num

        return ans      
'''
            
            
            
            
            
            
