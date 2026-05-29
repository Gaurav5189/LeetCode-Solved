
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dir={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        total=0
        max_seen=0

        if len(s) == 1:
            return dir[s[0]]
        else:
            for i in s[::-1]:
                value=dir[i]
                if value < max_seen:
                    total = total - value
                else:
                    total += value
                    max_seen=value
            return total
