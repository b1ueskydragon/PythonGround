class Solution:
    def findLongestWord(self, s: str, d: [str]) -> str:
        largest_bit = 0
        word = "plea"
        i = 0
        for c in s:
            largest_bit <<= 1
            if i < len(word):
                if word[i] == c:
                    largest_bit += 1
                    i += 1

        return bin(largest_bit)[2:]


if __name__ == '__main__':
    x = Solution()
    s = "abpcplea"
    res = x.findLongestWord(s, ["ale", "apple", "monkey", "plea"])
    print(''.join(map(lambda _: "1", s)))
    print(res)
