class Solution:
    def findLongestWord(self, s: str, d: [str]) -> str:
        bit_word = {}
        for _, word in enumerate(d):
            i = 0
            curr_bit = 0
            for c in s:
                curr_bit <<= 1
                if i < len(word):
                    if word[i] == c:
                        curr_bit += 1
                        i += 1
            if len(word) != i:
                continue
            if curr_bit:
                bit_word[curr_bit] = min(bit_word[curr_bit], word) if curr_bit in bit_word else word
        # print(bit_word)
        res = ""
        for k, v in bit_word.items():
            res = min(res, v) if len(res) == len(v) else max(res, v, key=len)
        return res
