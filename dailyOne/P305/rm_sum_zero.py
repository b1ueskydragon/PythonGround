"""
TODO:
  Replace to LinkedList and a Node
  that has value itself and, prev and next pointers.
"""


def solve(lst):
    # jump to next head. not necessary remove elements.

    if not lst:
        return []

    acc = 0
    head = 0
    i = head + 1

    if lst[head] == 0:
        return solve(lst[head + 1:])

    while i < len(lst):
        acc += lst[i]
        i += 1
        if acc == 0:
            return solve([lst[head]] + lst[i:])
        if acc + lst[head] == 0:
            return solve(lst[i:])

    return lst


# linked list
given = [3, 4, -7, 5, -6, 6]
print(solve(given))  # 5

given00 = [5, -6, 6, 7]
print(solve(given00))  # 5, 7

given01 = [0, 4, -7, 7, 3, 8]
print(solve(given01))  # 4, 3, 8

given02 = [4, -7, 7, 3, -3, -8, -10]
print(solve(given02))  # 4, -8, -10

given03 = [1, 1, -1, -1, 2, 2, 3, 3]
print(solve(given03))  # 2, 2, 3, 3

given04 = [0, 1, -1]
print(solve(given04))  # []

given05 = [1, 2, 3, 4, -3, -1]
print(solve(given05))  # bug