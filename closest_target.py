# 2515. Shortest Distance to Target String in a Circular Array (easy)
class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        if target == words[startIndex]:
            return 0

        n = len(words)
        dist = 0
        start_right = start_left = startIndex

        for _ in range(n // 2 + 1):
            if target == words[start_right] or target == words[start_left]:
                return dist
            else:
                start_right = (start_right + 1) % n
                start_left = (start_left - 1) % n
                dist+=1

        return -1
                
