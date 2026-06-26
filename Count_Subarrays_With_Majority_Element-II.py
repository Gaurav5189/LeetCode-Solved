# 3739. Count Subarrays With Majority Element II (Hard)
# using State Mapping with Prefix Sums(+1/-1 math)
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        counts = defaultdict(int)
        counts[0] = 1

        counter = 0
        subarr = 0
        temp_count = 0
        
        for n in nums:
            if n == target:
                temp_count += counts[counter]
                counter += 1
            else:
                counter -= 1
                temp_count -= counts[counter]

            subarr += temp_count
            counts[counter] += 1

        return subarr
