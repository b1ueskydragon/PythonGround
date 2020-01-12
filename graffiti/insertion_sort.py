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
