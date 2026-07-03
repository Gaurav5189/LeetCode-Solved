# 80. Remove Duplicates from Sorted Array II (medium)
# My first solution. Tc - O(NlogN), Sc - O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        counter = 0
        over = 0

        for i, v in enumerate(nums):
            if l != v:
                l = v
                counter = 1
            else:
                if counter >= 2:
                    nums[i] = 100000
                    over += 1
                else:
                    counter += 1
        
        nums.sort()
        del nums[len(nums)-over:]

        return len(nums)

# optimal Tc - O(n), Sc- O(1) solution using two pointer
'''
class Solution(object):
    def removeDuplicates(self, nums):
        l = len(nums)
        if l <= 2:
            return l

        count = 2

        for i in range(2, l):
            if nums[i] != nums[count-2]:
                nums[count] = nums[i]
                count += 1

        return count
'''
