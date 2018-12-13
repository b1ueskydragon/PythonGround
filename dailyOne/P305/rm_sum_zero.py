"""
TODO:
  Replace to LinkedList and a Node
  that has value itself and, next pointers.
"""


def solve(lst):
    # jump to next head.

    start = 0
    res = []
    while start < len(lst):
        curr = start
        acc = 0
        skip = False

        while curr < len(lst):
            acc += lst[curr]
            if acc == 0:
                start = curr
                skip = True
                break

            curr += 1

        if not skip:
            res.append(lst[start])  # printout

        start += 1

    return res


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
print(solve(given05))  # 1, 2, 3
