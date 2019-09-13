class Solution:
    def findLongestWord(self, s: str, d: [str]) -> str:
        curr_bit = largest_bit = 0
        for i, word in enumerate(d):
            i = 0
            for c in s:
                curr_bit <<= 1
                if i < len(word):
                    if word[i] == c:
                        curr_bit += 1
                        i += 1

            largest_bit = max(largest_bit, curr_bit)
            curr_bit = 0

        return bin(largest_bit)[2:]


if __name__ == '__main__':
    x = Solution()
    s = "abpcplea"
    res = x.findLongestWord(s, ["ale", "apple", "monkey", "plea"])
    print(''.join(map(lambda _: "1", s)))
    print(res)
