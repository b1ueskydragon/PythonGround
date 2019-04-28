"""
O(N^3) retrieval time
pruning with skip and break.
"""


class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplication
                continue
            if nums[i] * 4 > target:  # since nums are sorted
                break

            for j in range(i + 1, len(nums) - 2):
                # duplication already skipped, so i + 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[j] * 3 > target - nums[i]:
                    break

                low, high = j + 1, len(nums) - 1

                while low < high:
                    _sum = nums[i] + nums[j] + nums[low] + nums[high]

                    if _sum > target:
                        high -= 1
                    elif _sum < target:
                        low += 1
                    else:
                        res.append([nums[i], nums[j], nums[low], nums[high]])

                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1

                        low += 1
                        high -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(s.fourSum([0, 0, 0, 0], 0))
