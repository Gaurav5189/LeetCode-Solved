# 274. H-Index (medium)
# Tc- O(nlogn), Sc- O(1)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        counter = 1

        for i in citations:
            if i >= counter:
                counter += 1
            else:
                break

        return counter - 1
