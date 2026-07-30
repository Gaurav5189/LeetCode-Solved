# 3014. Minimum Number of Pushes to Type Word I (easy)
# used indexing. Tc and Sc- O(1)
class Solution(object):
    def minimumPushes(self, word):
        count = len(word)
        
        if count <= 8:
            return count
        elif count <= 16:
            return 8 + (count - 8) * 2
        elif count <= 24:
            return 24 + (count - 16) * 3
        else:
            return 48 + (count - 24) * 4
