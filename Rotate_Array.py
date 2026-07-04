# 189. Rotate Array (medium)
# 1st solution (Tc- O(n), Sc- O(n))
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        result = [0]*l

        for i in range(l):
            index = (i+k) % l
            result[index] = nums[i]

        nums[:] = result

'''
Alternative find but same complexity
class Solution(object):
    def rotate(self, nums, k):
        l = len(nums)
        k = k % l

        nums[:] = nums[-k:] + nums[:-k]
'''

# Optimal solution (Tc- O(n), Sc - O(1))
'''
class Solution(object):
    def rotate(self, nums, k):
        l = len(nums)
        k = k % l

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        
        reverse(0, l-1)
        reverse(0, k-1)
        reverse(k, l-1)
'''
