from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_inplace(xs: List[int], l: int, r: int) -> None:
            while l <= r:
                xs[l], xs[r] = xs[r], xs[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n  # since there's no constraint about k < n
        reverse_inplace(nums, 0, n - 1)
        reverse_inplace(nums, 0, k - 1)
        reverse_inplace(nums, k, n - 1)
