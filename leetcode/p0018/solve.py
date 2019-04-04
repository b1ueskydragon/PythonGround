class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        # I/O
        # input; 同一要素を含んだ not sorted ints
        # output; 最大で nC4 通り

        # Plan
        # sort first (同一要素を飛ばすため)
        # depth first search (線形で末尾まで探索, 構成できなかったら一つ戻る)

        # TODO divide

        return


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
