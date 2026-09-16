# 1385. Find the Distance Value Between Two Arrays (easy)
# Tc- O(nlogm), Sc- O(1)
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        result = 0

        for i in arr1:
            left = 0
            right = len(arr2) - 1
            found_invalid = False

            while left <= right:
                mid = (left+right) // 2

                if abs(arr2[mid]-i) <= d:
                    found_invalid = True
                    break
                elif arr2[mid] < i:
                    left = mid + 1
                else:
                    right = mid - 1
                    

            if not found_invalid:
                result += 1


        return result
