class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
                return [seen[need], i]
            
            seen[nums[i]] = i
            
nums = [3,3]
target = 6

sum1=Solution()
print(sum1.twoSum(nums, target))