# 1833. Maximum Ice Cream Bars (medium)
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        max_ice = 0

        costs.sort()

        for i, v in enumerate(costs):
            if v <= coins:
                max_ice += 1
                coins -= v
            else:
                break
        
        return max_ice


# using counting sorting(according to problem instruction) instead of python sort function
'''
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        n = len(costs)
        max_cost = max(costs)

        freq = [0] * (max_cost+1)

        for v in costs:
            freq[v] += 1

        for i in range(1, max_cost+1):
            freq[i] += freq[i-1]

        sorted_costs = [0] * n
        for i in range(n-1, -1, -1):
            v = costs[i]
            sorted_costs[freq[v] - 1] = v
            freq[v] -= 1

        max_ice = 0

        for i, v in enumerate(sorted_costs):
            if v <= coins:
                max_ice += 1
                coins -= v
            else:
                break
        
        return max_ice
'''
