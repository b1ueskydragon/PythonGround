"""
Given a number in the form of a list of digits, return all possible permutations.
"""


def permutations(nums):
    if not nums:
        return [[]]
    res = []  # should be local to refresh (need to append to prev res)
    for i, head in enumerate(nums):
        rems = nums[:i] + nums[i + 1:]
        prev_res = permutations(rems)
        for ps in prev_res:  # append to prev res
            res.append([head] + ps)
    return res
