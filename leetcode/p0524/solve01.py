class Solution:
    def findLongestWord(self, s: str, d: [str]) -> str:
        bit_word, res = {}, ""
        for _, word in enumerate(d):
            i, bit = 0, 0
            for c in s:
                bit <<= 1
                if i < len(word) and c == word[i]:
                    bit += 1
                    i += 1
            if len(word) != i:
                continue
            bit_word[bit] = word

        for k, v in bit_word.items():
            res = min(res, v) if len(res) == len(v) else max(res, v, key=len)
        return res
