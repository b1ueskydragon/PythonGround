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
        x2y, y2x = dict(), dict()
        for i in range(len(s)):
            x, y = s[i], t[i]
            if x not in x2y:
                x2y[x] = y
            elif x2y[x] != y:
                return False
            if y not in y2x:
                y2x[y] = x
            elif y2x[y] != x:
                return False
        return True
