# 1189. Maximum Number of Balloons (easy)
# My First Solution
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b, a, l, o, n = 0,0,0,0,0
        count = 0

        for i in text:
            b += 1 if i == 'b' else 0
        for i in text:
            a += 1 if i == 'a' else 0
        for i in text:
            l += 1 if i == 'l' else 0
        for i in text:
            o += 1 if i == 'o' else 0
        for i in text:
            n += 1 if i == 'n' else 0

        while True:
            if b >= 1 and a >= 1 and l >= 2 and o >= 2 and n >= 1:
                count += 1
                b -= 1
                a -= 1
                l -= 2
                o -= 2
                n -= 1
            else:
                break
        
        return count


# Better Alternative solution
'''
class Solution(object):
    def maxNumberOfBalloons(self, text):
        b=text.count('b')
        a=text.count('a')
        l=text.count('l')//2
        o=text.count('o')//2
        n=text.count('n')
        return min(b,a,l,o,n)
'''
