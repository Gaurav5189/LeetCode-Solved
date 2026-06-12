# 66. Plus One (easy)
# first attempt
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        all_nine = False

        for i in digits:
            if 9 == i:
                all_nine = True
            else:
                all_nine = False
                break
        if all_nine == True:
            for i in range(l):
                digits[i] = 0
            digits.insert(0, 1)
            return digits

        for i in range(l-1, -1, -1):
            if 9 == digits[i]:
                digits[i] = 0
                continue
            else:
                digits[i] += 1
                break

        return digits


# second attempt (optimized)
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)

        for i in range(l-1, -1, -1):
            if 9 > digits[i]:
                digits[i]+=1
                return digits

            digits[i] = 0

        return [1] + digits
'''
