class Solution:
    #  the number of smaller than the current number == the number of ordering ascendant.
    # O(N logN) Time O(N) Space.
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        order = dict()
        for i, v in enumerate(sorted(nums)):
            if v not in order:  # since duplicated numbers exist. set a first appeared i as the order num.
                order[v] = i
        return [order[x] for x in nums]
