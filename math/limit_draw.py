import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 3 * x ** 2 + 4 * x - 5


def f_dif(x):
    """
    上記の導関数
    """
    return 6 * x + 4


# x の範囲
x = np.linspace(-3, 3)
y = f(x)

# x = 1 のときの接戦
a = 1

"""
接線の方程式
点 (a, b) 傾 m
y - b = m(x - a) 

点 (a, f(a) 勾配 f`(a)
y = f`(a)x + f(a) - f`(a)a
"""
y_t = f_dif(a) * x + f(a) - f_dif(a) * a

plt.plot(x, y, label="y")
plt.plot(x, y_t, label="y_t")

plt.legend()
plt.show()
