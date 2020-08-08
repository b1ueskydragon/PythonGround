# sqrt -> O(logN)
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        mid = 0
        while left <= right:
            mid = left + (right - left) // 2  # to prevent overflow
            candidate = x // mid
            if candidate == mid:
                return mid
            elif mid > candidate:  # 5 * 5 > 9
                right = mid - 1
            else:
                left = mid + 1
        return right
