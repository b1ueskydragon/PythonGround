# All given inputs are in lowercase letters a-z, and "".
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        # edge cases.
        if not strs:
            return ""
        N = len(strs)
        if N == 1:
            return strs[0]
        # extra O(k) space, k is the length of head word.
        D = list(map(lambda x: [x, 0], strs[0]))
        if not D:
            return ""
        k = len(D)
        for i in range(1, N):  # O(N) time
            if not strs[i]:
                return ""
            if D[0][0] != strs[i][0]:
                return ""
            # O(l) time, l is the average length of word.
            for j, c in enumerate(strs[i]):
                if j >= k:
                    continue
                if D[j][0] == c:
                    D[j][1] += 1
        count = D[0][1]
        if count < 1:
            return ""
        p = ""
        for d in D:  # O(k) time.
            if d[1] != count:
                break
            p += d[0]
        return p

# Edge test cases
# ["", "a"]
# ["a", ""]
# ["a", "a", "b"]
