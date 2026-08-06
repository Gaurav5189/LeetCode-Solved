# 3345. Smallest Divisible Digit Product I (easy)
# Tc- O(logn), Sc- O(n)
class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            product = 1
            for i in str(n):
                product *= int(i)

            if product%t == 0:
                return n
            else:
                n+=1
