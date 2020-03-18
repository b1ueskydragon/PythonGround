"""
Given a SORTED array nums, remove the duplicates in-place 
such that each element appear only once and return the new length.
"""


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if not nums:
            return 0
        head = nums.pop(0)  # 0
        # nums [0,1,1,1,2,2,3,3,4]
        nums.append(head - 1)  # sentinel
        while head <= nums[0]:
            while head == nums[0]:
                nums.pop(0)
            else:
                # should not be popped, so append to last and wait to come front (¬since we should do it in-place).
                nums.append(head)
            # print(nums)
            head = nums.pop(0)  # update
        else:
            # remove sentinel and append dropped elem.
            nums.pop(0)
            nums.append(head)
        return len(nums)  # at this point, nums doesn't have the duplicates.


"""
for checking the function was proceeded in-place...

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

if __name__ == '__main__':
    a = Solution()
    a.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
