class Solution:
    def compress(self, chars: [str]) -> int:
        i, j = 0, 1
        flag = chr(32)
        chars.append(flag)
        while True:
            if chars[i] == flag:
                break
            if chars[i] == chars[j]:
                j += 1
            else:
                chars.append(chars[i])
                if j - i != 1:
                    for _ in str(j - i):
                        chars.append(_)
                j += 1
                i = j - 1

        while chars[0] != flag:
            chars.pop(0)
        chars.pop(0)
        return len(chars)
