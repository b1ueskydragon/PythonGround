class Solution:
    """
    1)  Transpose        [[a0,b0], [a1,b1]..., [an,bn]] => [[a0,...,an], [b0,...,bn]]
    2)  Difference set   (Group b) `diff` (Group a)
    2') if 2) is `zero`, return -1 . (the number of result element in Group b) < (N-1), return -1.
    """

    def findJudge(self, N: int, trust: [[int]]) -> int:
        if not trust:
            return N
        group = list(map(list, zip(*trust)))
        a, b = group
        diff = set(b) - set(a)
        if len(diff) == 1:
            unq = diff.pop()
            if len(list(filter(lambda _: _ == unq, b))) == N - 1:
                return unq
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(N=1, trust=[]))
    print(s.findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))
    print(s.findJudge(N=3, trust=[[1, 2], [2, 3]]))  # 1->3 not exists, return -1
    print(s.findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
