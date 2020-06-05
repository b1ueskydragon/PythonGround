class Solution:
    def videoStitching(self, clips: [[int]], T: int) -> int:
        end_points = [0] * 101  # can have extra video after the event ends. constraint T<=100
        for start, end in clips:
            end_points[start] = max(end, end_points[start])
        end_before = reachable = count = 0
        for t in range(T + 1):
            if t > reachable:  # has a blank(fragmentation)
                return -1
            reachable = max(reachable, end_points[t])
            if t < end_before:
                continue
            count += 1
            end_before = reachable
            if end_before >= T:  # reachable already exceed T at this point
                return count
        return -1
