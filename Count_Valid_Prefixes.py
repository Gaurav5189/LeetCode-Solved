# Biweekly Contest 188 - Q1 Count Valid Prefixes (easy)
# Tc- O(n), Sc- O(1)
class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        one = zero = count = 0
        
        for i in range(len(s)):
            if int(s[i]) == 0:
                zero += 1
            else:
                one += 1

            if abs(one-zero) <= 1:
                count +=1

        return count
