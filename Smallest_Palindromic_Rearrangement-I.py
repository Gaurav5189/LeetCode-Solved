# 3517. Smallest Palindromic Rearrangement I (medium)
# Counting/Sorting method. Tc- O(nlogn), Sc- O(n)
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        char = set(s)
        res = middle = ""

        for l in char:
            if s.count(l)%2 == 1 and s.count(l) > 2:
                middle = l
                res += l * (s.count(l)//2)
            elif s.count(l)%2 == 1 and s.count(l) < 2:
                middle = l
            else:
                res += l * (s.count(l)//2)

        res = "".join(sorted(res))
        reverse_res = res[::-1]

        return res + middle + reverse_res
