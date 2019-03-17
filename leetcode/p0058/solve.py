class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        return len(l[-1]) if l else 0


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord(s="Hello World"))  # 5
    print(s.lengthOfLastWord(s=" "))  # 0
    print(s.lengthOfLastWord(s="Hello World "))  # 5
