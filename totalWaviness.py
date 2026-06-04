# 3751. Total Waviness of Numbers in Range I (medium level)
class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        waviness=0

        for i in range(num1, num2 + 1):
            i_str = str(i)

            if len(i_str) < 3:
                continue

            for x in range(1, len(i_str)-1):
                if int(i_str[x-1]) < int(i_str[x]) > int(i_str[x+1]):
                    waviness+=1
                elif int(i_str[x-1]) > int(i_str[x]) < int(i_str[x+1]):
                    waviness+=1

        return waviness
