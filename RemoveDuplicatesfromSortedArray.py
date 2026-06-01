class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=len(nums)
        if total == 0:
            return 0

        current_value = None
        k=0

        for i in range(total):
            if current_value == nums[i]:
                continue
            else:
                current_value = nums[i]
                nums[k] = nums[i]
                k+=1

        return k
