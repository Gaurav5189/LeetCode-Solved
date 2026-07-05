# 121. Best Time to Buy and Sell Stock (easy)
# used dynamic programing(Kadane's Algorithm). Tc- O(n), Sc- O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = float('inf')

        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > profit:
                profit = p - min_price

        return profit
