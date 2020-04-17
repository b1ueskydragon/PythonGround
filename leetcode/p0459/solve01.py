class Solution:
    @staticmethod
    def skip_table(sub_str):
        table = [0] * len(sub_str)
        # if the pattern matched until n th char ( i, j ∈ n ), then we can make a k skip.
        # the table should be [k1, ... , kn]
        i, j = 0, 1  # j is faster than i. both of cursors will retrieval inside of sub_str.
        while j < len(sub_str):
            if sub_str[i] == sub_str[j]:
                table[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    table[j] = 0
                    j += 1
                else:  # if i and j not matched rewind i.
                    i -= 1  # j should wait and will find a skip count on the next loop.
        return table

    def repeatedSubstringPattern(self, s: str) -> bool:
        return False
