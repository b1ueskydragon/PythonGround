class Solution:
    def letterCasePermutation(self, S):
        """
        cartesian product := {(a, b) | a ∈ A, b ∈ B}
        """
        import itertools
        t_cartesian = [[s.lower(), s.upper()] if s.isalpha() else s for s in S]
        print(t_cartesian)
        print(list(itertools.product(*t_cartesian)))


if __name__ == '__main__':
    x = Solution()
    x.letterCasePermutation("ab")
