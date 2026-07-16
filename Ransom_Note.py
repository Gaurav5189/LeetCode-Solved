# 383. Ransom Note (easy)
# Tc- O(r+m), Sc- O(1)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_map1 = Counter(ransomNote)
        char_map2 = Counter(magazine)

        result = not (char_map1 - char_map2)

        return result
