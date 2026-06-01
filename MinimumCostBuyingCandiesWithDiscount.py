# my solution
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #edge case
        if 2 >= len(cost):
            if 1 >= len(cost):
                return cost[0]
            else:
                sum=0
                for i in range(len(cost)):
                    sum+=cost[i]
                return sum

        cost.sort(reverse=True)
        
        Total=0
        for i in range(len(cost)):
            if (i+1) % 3 != 0:
                Total+=cost[i]
        return Total


# other different approch
'''
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        s=0
        took=0 
       
        for i in range(len(cost)-1,-1,-1):
            if took==2:
                took=0 
                
            else:
                s+=cost[i]
                took+=1 

            
        return s
'''
