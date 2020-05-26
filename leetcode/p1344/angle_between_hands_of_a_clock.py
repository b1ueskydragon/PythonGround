"""
Each hour's and minutes's moving angle per 1 min.
per 1 min; h += 0.5 , m += 6

cases:
 - hour 12
    - only accumulate minute's degree
 - hour between 1 .. 5 (hour's degree < 180)
    |min - hour|
        - smaller or equal as 180 (3:10, 3:20 ..)
        - larger than 180 (3:54 ..)
 - hour between 6 .. 11. (hour's degree is >= 180)
     |min - hour|
         - smaller or equal as 180 (7:54 ..)
         - larger than 180 (9:13 ..)
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_degrees = dict()
        hour_degrees[12] = 0
        for h in range(1, 12):
            hour_degrees[h] = 30 * h
        fast = 6.0 * minutes  # min
        slow = hour_degrees[hour] + 0.5 * minutes  # hour
        if hour_degrees[hour] < 180:
            angle = abs(fast - slow)
            if angle <= 180:
                return angle
            else:
                return (360 - fast) + slow
        else:
            angle = abs(slow - fast)
            if angle <= 180:
                return angle
            else:
                return (360 - slow) + fast
