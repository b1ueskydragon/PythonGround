class Solution:
    def findLongestWord(self, s: str, d: [str]) -> str:
        from collections import deque
        gen_word = ""
        longest_word = gen_word  # dp

        for word in d:
            chars = deque(s)
            i = 0
            while chars and i < len(word):
                curr = chars.popleft()
                if curr == word[i]:
                    gen_word += curr
                    i += 1

            if word == gen_word:
                if len(gen_word) == len(longest_word):
                    longest_word = min(gen_word, longest_word)
                else:
                    longest_word = max(gen_word, longest_word, key=len)
            gen_word = ""

        return longest_word
