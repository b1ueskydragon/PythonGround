class Solution:
    def videoStitching(self, clips: [[int]], T: int) -> int:
        end_points = [0] * 101  # farthest from each start point. constraint T<=100
        for start, end in clips:
            end_points[start] = max(end, end_points[start])
        end_before = reachable = count = 0
        for curr in range(T + 1):
            if curr > reachable:  # has a blank(fragmentation)
                return -1
            reachable = max(reachable, end_points[curr])
            if curr >= end_before:
                count += 1
                end_before = reachable
                if end_before >= T:  # reachable already exceed T at this point
                    return count
        return -1
