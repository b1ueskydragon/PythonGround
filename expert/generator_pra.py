"""
Expert Python Programming page 65
Sample code
"""


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib = fibonacci()

print(next(fib))  # 1
print(next(fib))  # 1
print(next(fib))  # 2
print(next(fib))  # 3

print([next(fib) for i in range(10)])
