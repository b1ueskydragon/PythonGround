class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        valid = 0
        for i, c in enumerate(s, start=1):
            if i < n and c == "(" and s[i] == ")":
                valid += 2

        return n - valid


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid(s="((())"))  # 1
    print(s.minAddToMakeValid(s="()()"))  # 0
    print(s.minAddToMakeValid(s="()((()))"))  # 0
