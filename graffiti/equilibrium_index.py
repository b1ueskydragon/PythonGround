def solve(nums, n):
    if not nums:
        return -1
    if n > 2:
        i = 1
        left = sum(nums[:i])
        right = sum(nums[i + 1:])

        while n > i and left != right:
            i += 1
            left += nums[i - 1]
            if n > i:
                right -= nums[i]
        else:
            if n > i:
                return i
    return -1


print(solve(nums=[2, 1, 2, -3, 4, -2, -3, 4], n=8))
print(solve(nums=[0, -2147483648, 0, -2147483648], n=4))
print(solve(nums=[0, -2147483648, 0, 2147483648], n=4))
