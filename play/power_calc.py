"""
高速累乗計算
x: 基数
n: 乗
"""


# O(logN)
def power_calc(x, n):
    if n % 2 == 0:
        return (x ** 2) ** int(n / 2)
    else:
        return x * (x ** (n - 1))


print(power_calc(3, 11))
