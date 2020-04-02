# Binary search. Discard the second half of the string.
# Using additional memory to generate substring but fast.
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""

        def is_all_have(pref):
            for s in strs:
                if not s.startswith(pref):
                    # discard immediately.
                    return False
            return True

        # At first, find a minimal length (this will be the maximum bound).
        min_len = min(map(lambda x: len(x), strs))
        low = 1
        high = min_len
        s = strs[0]  # Anything is ok. and access to head is O(1).
        while low <= high:  # adjust range (low and high).
            p = (low + high) // 2
            if is_all_have(s[:p]):
                low = p + 1  # get broader
            else:
                high = p - 1  # get narrower
        return s[:(low + high) // 2]
