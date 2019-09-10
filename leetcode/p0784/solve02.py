class Solution:
    def letterCasePermutation(self, S):
        """
        cartesian product := {(a, b) | a ∈ A, b ∈ B}
        """
        import itertools
        pairs = [[s.lower(), s.upper()] if s.isalpha() else s for s in S]
        return list(map(lambda l: ''.join(l), itertools.product(*pairs)))
