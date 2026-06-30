# 1358. Number of Substrings Containing All Three Characters (medium)
# Sliding window TC - O(n) & SC - O(1)
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {'a':0, 'b':0, 'c':0}
        l = len(s)
        result = 0

        i = 0
        j = 0

        while j < l:
            ch = s[j]
            seen[ch] += 1

            while (seen['a'] > 0 and seen['b'] > 0 and seen['c'] > 0):
                result += (l - j)

                seen[s[i]] -= 1
                i+=1
            
            j+=1

        return result
