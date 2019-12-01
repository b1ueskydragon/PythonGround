"""'
Demonstration of mathematical approach :)

origin source;
https://www.quora.com/How-can-I-print-1-to-100-in-C%2B%2B-without-a-loop-goto-or-recursion?ch=10&share=9b09c507&srid=Jqvc
"""


def f(x):
    # take the derivative of 1 / (1 - x)
    # 1/(1-x) = x^0 + x^1 + x^2 + x^3 +... (infinite)
    return (1 - x) ** -2


print(f(0.01))
print(f(0.001))

print((1 / (99 ** 2)) / 100)
print((1 / (999 ** 2)) / 100)


def numbers(N, x=0.001):
    acc = 0
    for n in range(N + 1):
        print(acc)
        acc += n * (x ** (n - 1))


numbers(8)
