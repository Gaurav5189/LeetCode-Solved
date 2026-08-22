# 3622. Check Divisibility by Digit Sum and Product (easy)
# Tc & SC - O(logn)
class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c = str(n)
        s = 0
        p = 1

        for i in c:
            s += int(i)
            p *= int(i)

        if n%(s+p) == 0:
            return True

        return False


# using Pure math(no str conversion)
# Tc- O(logn), Sc- O(1)
'''
class Solution(object):
    def checkDivisibility(self, n):
        hold = n
        s = 0
        p = 1

        while(n>0):
            i = n%10
            s += i
            p *= i
            n = n//10

        return hold%(s+p)==0
'''
