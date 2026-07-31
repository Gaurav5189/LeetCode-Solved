# 28. Find the Index of the First Occurrence in a String (easy)
# using sliding window. Tc- O(n+m), Sc- O(m)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        for i in range(0, len(haystack)-l+1):
            if haystack[i:i+l] == needle:
                return i
        
        return -1
