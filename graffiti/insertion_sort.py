def insertion_sort(nums):
    """ in-place """
    for i in range(1, len(nums)):
        fixed_ahead = nums[i]
        j = i - 1  # followed
        while j > -1 and nums[j] > fixed_ahead:
            nums[j + 1] = nums[j]
            nums[j] = fixed_ahead
            j -= 1  # write back
    return nums
