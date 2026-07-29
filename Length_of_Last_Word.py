# 58. Length of Last Word (easy)
# simple version. Tc and Sc - O(n)
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()

        return len(words[-1])

# Alternative single pointer solution. Tc- O(n), Sc- O(1)
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l =  len(s) - 1
        count = 0

        while l>=0 and s[l] == ' ':
            l -= 1

        while l>=0 and s[l] != ' ':
            count += 1
            l -= 1

        return count
'''
