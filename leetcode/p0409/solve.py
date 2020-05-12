class Solution:
    # focus on the `longest` and the `length`
    # There's only two pattern in palindrome, all is even or, includes just one case odd.
    # O(N) time and space.
    def longestPalindrome(self, s: str) -> int:
        count = dict()
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        size, odd = 0, 0
        for v in count.values():
            if v % 2 == 0:
                size += v
            else:
                size += (v - 1)
                odd += 1
        return (size, size + 1)[odd > 0]  # only one type and one of odd could be included if exist.
