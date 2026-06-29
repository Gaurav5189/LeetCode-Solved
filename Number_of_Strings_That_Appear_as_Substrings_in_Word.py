# 1967. Number of Strings That Appear as Substrings in Word (easy)
# TC - O(N x K) and SC - O(1)
class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        match = 0

        for s in patterns:
            match += 1 if s in word else 0

        return match
