class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> [str]:
        res = []
        words = text.split()
        for i, word in enumerate(words, start=1):
            if i < len(words) - 1 and word == first and words[i] == second:
                res.append(words[i + 1])

        return res
