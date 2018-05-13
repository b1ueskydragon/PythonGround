"""
return x if b is 1 and y if b is 0
using only mathematical or bit operations
"""


def assume(x, y, b):
    """
     initial approach
     Imagine a linear equation graph.

     f(x) = bx + y (constant y is y-intercept)
     if b is 0, f(x) = y
     if b is 1, f(x) = x + y
    """
    return x * b + y * (1 - b)


print(assume(3, 5, 1))
print(assume(3, 5, 0))
