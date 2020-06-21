class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n != 0:  # edge case?
            nums1[0] = nums2[0]
        k = m + n - 1  # rightmost index of zero that can hold an element from nums2.
        i = m - 1
        j = n - 1
        while 0 <= i:
            if 0 <= j and nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k], nums1[i] = nums1[i], nums1[k]  # move zero to the leftside in nums1.
                i -= 1
            k -= 1
        while 0 <= j and 0 <= k:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        # There's no need to consider negative elements, maybe.
