class Solution:
    """
    formed by deleting some characters of the given string
    e. g.)

    abpcplea
    a____le_ # ale
    a_p_ple_ # apple
    ____plea # plea
    ________ # monkey
    """

    def findLongestWord(self, s: str, d: [str]) -> str:
        from collections import deque
        longest_word = ""  # dp
        sample = "ale"
        chars = deque(s)
        i = 0
        while chars and i < len(sample):
            curr = chars.popleft()
            if curr == sample[i]:
                longest_word += curr
                i += 1

        print(longest_word)
        return ""


if __name__ == '__main__':
    x = Solution()
    res = x.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"])
