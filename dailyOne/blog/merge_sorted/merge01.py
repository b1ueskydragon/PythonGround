"""
Same strategy as merge.py
 - Refactor only (index scan to pop head, to one line)
"""


def merge(left, right):
    def _merge(left, right):
        while left and right:
            yield left.pop(0) if left[0] <= right[0] else right.pop(0)

        while left:
            yield left.pop(0)

        while right:
            yield right.pop(0)

    return list(_merge(left, right))


def solve(groups, i):
    return [] if i < 1 else merge(groups[0], groups[1]) if i == 1 else merge(solve(groups, i - 1), groups[i])


"""
test cases
"""
print(merge([10, 15, 30], [12, 15, 20]))

given = [10, 15, 30], [12, 15, 20], [17, 20, 32]
given01 = [[3], [1, 2]]
given02 = [[1], []]
given03 = []

print(solve(given, len(given) - 1))
print(solve(given01, len(given01) - 1))
print(solve(given02, len(given02) - 1))
print(solve(given03, len(given03) - 1))
