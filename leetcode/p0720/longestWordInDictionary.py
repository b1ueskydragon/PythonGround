class Solution:
    def longestWord(self, words: [str]) -> str:
        max_word = ""
        prefixes = set(words)

        for word in words:
            longer = len(word) > len(max_word)
            smaller = len(word) == len(max_word) and word < max_word

            if longer or smaller:
                if all(word[:i] in prefixes for i in range(1, len(word))):
                    max_word = word

        return max_word
