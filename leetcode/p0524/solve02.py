class Solution:
    def __init__(self):
        self._dict = []

    def _make_dict(self, s):
        self._dict = [[-1] * 26] * (len(s) + 1)  # has sentinel
        for i in reversed(range(len(s))):
            self._dict[i] = self._dict[i + 1].copy()
            self._dict[i][ord(s[i]) - ord('a')] = i

    def _is_sub(self, word):
        row = 0
        for c in word:
            index = self._dict[row][ord(c) - ord('a')]
            if index == -1:
                return False
            row = index + 1

        return True

    def findLongestWord(self, s: str, d: [str]) -> str:
        self._make_dict(s)  # side effect
        longest_word = ""
        for word in d:
            if self._is_sub(word):
                if len(longest_word) < len(word) or len(longest_word) == len(word) and word < longest_word:
                    longest_word = word
        return longest_word


if __name__ == '__main__':
    x = Solution()
    x._make_dict("abcd")
    print(x._dict)
    res = x.findLongestWord("bab", ["ba", "ab", "a", "b"])
    print(res)
