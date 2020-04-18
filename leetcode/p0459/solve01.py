class Solution:
    @staticmethod
    def skip_table(string):
        table = [0] * len(string)
        # if the pattern matched until n th char ( i, j ∈ n ), then we can make a k skip.
        # the table should be [k1, ... , kn]
        i, j = 0, 1  # j is faster than i. both of cursors will retrieval inside of string.
        while j < len(string):
            if string[i] == string[j]:
                table[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:  # if i and j not matched rewind i.
                    # i -= 1 made too much skipping. we should skip more carefully.
                    i = table[i - 1]  # j should wait and will find a skip count on the next loop.
        return table

    def repeatedSubstringPattern(self, s: str) -> bool:
        table = Solution.skip_table(s)
        N, last = len(s), table[-1]  # N - last is the length of the minimal pattern.
        return last > 0 and N % (N - last) == 0
