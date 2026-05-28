# My Solution
class Solution(object):
    def isPalindrome(self, x):
        temp=x
        rev=0
        if x < 0:
            return False
        else:
            while temp!=0:
                digit = temp % 10
                rev = rev * 10 + digit
                temp = temp // 10

            return rev == x


# Best Solution

# class Solution(object):
#     def isPalindrome(self, x):
#         strx = str(x)
#         return strx == strx[::-1]