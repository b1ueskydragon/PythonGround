def insertion_sort(nums):
    """ in-place """
    for i in range(1, len(nums)):
        fixed_ahead = nums[i]
        j = i  # followed
        while j > 0 and nums[j - 1] > fixed_ahead:
            nums[j] = nums[j - 1]
            j -= 1  # write back
        nums[j] = fixed_ahead
    return nums


def insertion_sort_desc(nums):
    """ in-place """
    n = len(nums)
    min_int = -2147483648
    nums.append(min_int)  # sentinel to skip checking n > j

    for i in reversed(range(n - 1)):
        fixed_ahead = nums[i]
        j = i + 1
        while nums[j] > fixed_ahead:
            nums[j - 1] = nums[j]
            j += 1
        nums[j - 1] = fixed_ahead
    return nums[:-1]
