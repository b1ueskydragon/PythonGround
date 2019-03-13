class Solution:
    def reverse(self, x: int) -> int:
        cache = 0
        negate = x < 0
        x = abs(x)
        while x:
            # check overflow
            if not (-2147483648 <= cache <= 2147483647):
                return 0
            cache += (x % 10)
            x //= 10
            if x:
                cache *= 10
        return (cache, -cache)[negate]


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(x=123))
    print(s.reverse(x=-123))
    print(s.reverse(x=0))
    print(s.reverse(x=2 ** 31))
    print(s.reverse(x=-2 ** 31))
