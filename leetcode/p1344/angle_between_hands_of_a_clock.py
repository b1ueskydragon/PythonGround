"""
Each hour's and minutes's moving angle per 1 min;
h += 0.5 , m += 6.
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_degrees = dict()
        hour_degrees[12] = 0
        for h in range(1, 12):
            hour_degrees[h] = 30 * h
        fast = 6.0 * minutes  # min
        slow = hour_degrees[hour] + 0.5 * minutes  # hour
        angle = abs(slow - fast)
        if angle <= 180:
            return angle
        if hour_degrees[hour] < 180:
            return (360 - fast) + slow
        else:
            return (360 - slow) + fast
