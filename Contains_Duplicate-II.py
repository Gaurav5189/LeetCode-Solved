# 219. Contains Duplicate II (easy)
# Using sliding window
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()

        for i, v in enumerate(nums):
            if v in window:
                return True
            
            window.add(v)

            if len(window) > k:
                window.remove(nums[i-k])
        
        return False
