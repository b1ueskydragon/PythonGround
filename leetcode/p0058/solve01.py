class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        acc = 0
        _ascii = False
        for c in reversed(s):
            if c == ' ':
                if _ascii:
                    break
                else:
                    continue
            acc += 1
            _ascii = True
        return acc

    def lengthOfLastWord_(self, s: str) -> int:
        acc = 0
        for c in reversed(s):
            if c == ' ':
                if acc:
                    return acc
                else:  # a string but not found alpha yet
                    continue
            acc += 1
        return acc


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord(s="Hello World"))  # 5
    print(s.lengthOfLastWord(s=" "))  # 0
    print(s.lengthOfLastWord(s="Hello World "))  # 5

    print(s.lengthOfLastWord_(s="Hello World "))  # 5
