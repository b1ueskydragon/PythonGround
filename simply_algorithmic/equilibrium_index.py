def solve(nums, n):
    i = 1
    while sum(nums[:i]) != sum(nums[i + 1:]):
        i += 1
    else:
        return i


print(solve(nums=[-1, 3, -4, 5, 1, -6, 2, 1], n=8))
