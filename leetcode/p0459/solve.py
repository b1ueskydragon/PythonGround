class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)  # a pattern's max length is N // 2, at most.
        if N < 2:  # 'a'
            return False
        if len(set(s)) < 2:  # 'aa..a..a', 'bb'
            return True
        gcds = [i for i in range(2, N) if N % i == 0]
        for i in gcds:
            sub, rem = s[:i], s[i:]
            w = len(rem) // len(sub)
            if sub * w != rem:
                continue
            else:
                return True
        return False
