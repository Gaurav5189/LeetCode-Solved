# 628. Maximum Product of Three Numbers (easy)
# Tc and Sc - O(n)
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r_max = 1
        r_combined = 1
        temp = nums[:]

        for i in range(3):
            high = max(temp)
            r_max*=high
            temp.remove(high)

            if i == 0:
                r_combined = high

        for _ in range(2):
            low = min(nums)
            r_combined*=low
            nums.remove(low)

        return max(r_max, r_combined)


# Sc optimised solution. Tc-O(nlogn) and Sc- O(1)
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        all_max = nums[-1] * nums[-2] * nums[-3]
        combined_max = nums[-1] * nums[0] * nums[1]

        return max(all_max, combined_max)
        
