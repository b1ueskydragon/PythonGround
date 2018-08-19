import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -2 * x ** 2 + x + 3


def f_dif(x):
    return -4 * x + 1


x = np.linspace(-3, 3)
y = f(x)

a = 1
y_t = f_dif(a) * x - f_dif(a) * a + f(a)

plt.plot(x, y, label="y")
plt.plot(x, y_t, label="y_t")

plt.legend()
plt.show()
