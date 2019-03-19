class Solution:
    def _valid(self, s: str, l: int, r: int):
        """
        l, r are center indices. expands.
        """
        # empty string
        if s == "":
            return True
        # ()()...()()
        while l >= 0 and r < len(s) and s[l] == "(" and s[r] == ")":
            l -= 1
            r += 1

        #  ((...))

    def minAddToMakeValid(self, S: str) -> int:
        return


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid(S="())"))  # 1
    print(s.minAddToMakeValid(S="((("))  # 3
