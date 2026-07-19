# 290. Word Pattern (easy)
# Tc- O(n^2), Sc- O(n)

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_bind = {}
        word_bind = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in char_bind and char_bind[char] != word:
                return False
            if word in word_bind and word_bind[word] != char:
                return False

            char_bind[char] = word
            word_bind[word] = char

        return True
