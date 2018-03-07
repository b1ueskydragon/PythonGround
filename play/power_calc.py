# O(n)
def power_calc(x, n):
    if n % 2 == 0:
        return (x ** 2) ** int(n / 2)
    else:
        return x * (x ** (n - 1))


print(power_calc(3, 11))

"""
高速累乗計算
最低でも2回に1回は n のビット数が減る

x: 基数
n: 乗
"""


# O(log n)
def power(x, n):
    if n is 0:  # exit case
        return 1
    if n % 2 is 0:  # n が偶数: 半分にして次は偶数か奇数に
        return power(x ** 2, int(n / 2))
    else:  # n が奇数: 1を引いて次は必ず偶数
        return x * power(x, n - 1)


print(power(3, 11))
