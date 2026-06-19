# 1732. Find the Highest Altitude (easy)
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = [0]
        for i, v in enumerate(gain):
            temp = alt[i]
            alt.append(temp+v)

        return max(alt)
