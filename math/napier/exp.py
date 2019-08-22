"""
d/dx e^x = e^x
"""
import numpy as np
import matplotlib.pyplot as plt


def exp_f(x):
    base = 2
    return np.power(base, x)


def numerical_diff(f, x):
    h = 1e-2  # 0.001
    return (f(x + h) - f(x - h)) / (2 * h)  # mean-value theorem (to minimize error)


def draw_2(x_values):
    exp_values = exp_f(x_values)
    diff_values = numerical_diff(exp_f, x_values)

    plt.plot(x_values, exp_values, color="blue")
    plt.plot(x_values, diff_values, color="red")


def draw_e(x_values):
    # an approximation of Napier's constant
    plt.plot(x_values, np.power(2.718, x_values), color="green")
    plt.plot(x_values, numerical_diff(lambda x: np.power(2.718, x), x_values), color="yellow")


if __name__ == '__main__':
    xs = np.arange(-1, 1, 0.1)
    draw_2(xs)
    draw_e(xs)

    plt.grid()
    plt.show()
