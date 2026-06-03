# 3635. Earliest Finish Time for Land and Water Rides II (medium level) with Time complexity O(nlogn)
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        land_end_time = []
        for s, d in zip(landStartTime, landDuration):
            land_end_time.append(s+d)
        land_end_time = sorted(land_end_time)
        min_lfinish = land_end_time[0]

        min_ride_time = float('inf')

        for s, d in zip(waterStartTime, waterDuration):
            min_ride_time = min(min_ride_time, max(s, min_lfinish) + d)

        water_end_time = []
        for s, d in zip(waterStartTime, waterDuration):
            water_end_time.append(s+d)
        water_end_time = sorted(water_end_time)
        min_wfinish = water_end_time[0]

        for s, d in zip(landStartTime, landDuration):
            min_ride_time = min(min_ride_time, max(s, min_wfinish) + d)
        
        return min_ride_time
