class Solution:
    """
    Bijection.

    'paper', 'title'
    p -> t
    a -> i
    e -> l
    r -> e
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        def mapping(X, Y, N):
            cache = dict()
            i = 0
            while i < N:
                x, y = X[i], Y[i]
                if x not in cache:
                    cache[x] = y
                elif cache[x] != y:
                    return False
                i += 1
            return True

        N = len(s)
        return mapping(s, t, N) and mapping(t, s, N)
