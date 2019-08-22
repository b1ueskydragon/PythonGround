"""
d/dx e^x = e^x
"""
import numpy as np
import matplotlib.pyplot as plt


def exp_f(x):
    base = 2  # 2.718
    return np.power(base, x)


def numerical_diff(f, x):
    h = 1e-2  # 0.001
    return (f(x + h) - f(x - h)) / (2 * h)  # mean-value theorem (to minimize error)


def graph():
    x_values = np.arange(-1, 1, 0.1)
    exp_values = exp_f(x_values)
    diff_values = numerical_diff(exp_f, x_values)

    plt.plot(x_values, exp_values, color="blue")
    plt.plot(x_values, diff_values, color="red")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    graph()
