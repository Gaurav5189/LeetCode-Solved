# 88. Merge Sorted Array (easy)
# my original solution

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1) - 1, -1, -1):
            if 0!=nums1[i] or i == (m-1):
                break
            else:
                del nums1[i]

        nums1 += nums2

        nums1.sort()


# better alternative
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m]+nums2)
'''
