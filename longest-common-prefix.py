class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        fword = strs[0]

        for i in range(len(fword)):
            for item in strs[1:]:
                if len(item)<=i or fword[i] != item[i]:
                    return fword[:i]
        return fword
