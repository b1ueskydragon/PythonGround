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

            if curr_bit:
                if curr_bit in bit_word:
                    bit_word[curr_bit] = min(bit_word[curr_bit], word)
                else:
                    bit_word[curr_bit] = word
        return bit_word[max(bit_word)] if len(bit_word) > 0 else ""
