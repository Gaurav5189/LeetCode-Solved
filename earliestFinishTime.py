# 3633. Earliest Finish Time for Land and Water Rides
# My solution
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        min_finish_time = float('inf')
        
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                
                finish_land_first = landStartTime[i] + landDuration[i]
                start_water_second = max(finish_land_first, waterStartTime[j])
                final_water_finish = start_water_second + waterDuration[j]
                
                finish_water_first = waterStartTime[j] + waterDuration[j]
                start_land_second = max(finish_water_first, landStartTime[i])
                final_land_finish = start_land_second + landDuration[i]
                
                min_finish_time = min(min_finish_time, final_water_finish, final_land_finish)
                
        return min_finish_time



# Alternate approch --------------------------------------
'''
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        # Initialize with a very large number so any valid time will be smaller
        min_finish_time = float('inf')
        
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                
                finish_land_first = landStartTime[i] + landDuration[i]
                start_water_second = max(finish_land_first, waterStartTime[j])
                final_water_finish = start_water_second + waterDuration[j]
                
                finish_water_first = waterStartTime[j] + waterDuration[j]
                start_land_second = max(finish_water_first, landStartTime[i])
                final_land_finish = start_land_second + landDuration[i]
                
                min_finish_time = min(min_finish_time, final_water_finish, final_land_finish)
                
        return min_finish_time
'''
