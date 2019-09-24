class Solution:
    def __init__(self):
        self.dict = []

    def make_dict(self, s):
        self.dict = [[-1] * 26] * (len(s) + 1)  # has sentinel
        for i in reversed(range(len(s))):
            self.dict[i] = self.dict[i + 1].copy()
            self.dict[i][ord(s[i]) - ord('a')] = i

    def findLongestWord(self, s: str, d: [str]) -> str:
        longest_word = ""
        return longest_word


if __name__ == '__main__':
    x = Solution()
    x.make_dict("abcd")
    print(x.dict)
