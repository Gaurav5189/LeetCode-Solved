# 172. Factorial Trailing Zeroes (medium)
# Tc- O(n^2 logn), Sc- O(nlogn)
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0

        result = 1
        for i in range(1, n+1):
            result *= i

        zeros = 0
        result = str(result)
        for n in range(len(result)-1, -1, -1):
            if result[n] == '0':
                zeros += 1
            else:
                break

        return zeros

# Alternative approach. Tc- O(log5n), Sc- O(1)
# Ex- 10! = has 2 trailing zero and 50! has 12 trailing zero - thats why we floor divide it by 5(50//5 = 10 then 10//5 = 2, therefore: 10+2=12)
'''
class Solution(object):
    def trailingZeroes(self, n):
        count = 0

        while n>=5:
            n //= 5
            count += n

        return count
'''
