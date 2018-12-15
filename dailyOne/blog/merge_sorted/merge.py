# k = 3  # k sorted lists
# n = 3  # each with size n


def merge(left, right):
    def _merge(left, right):
        """
        Conquer

        :param left: list (sorted)
        :param right: list (sorted)
        :return: merged list
        """
        l, r = 0, 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                yield left[l]
                l += 1
            else:
                yield right[r]
                r += 1

        while l < len(left):
            yield left[l]
            l += 1

        while r < len(right):
            yield right[r]
            r += 1

    return list(_merge(left, right))


def solve(groups, i):
    """
    TODO: make fold function
    """
    if i < 1:  # edge case
        return []

    if i == 1:
        return merge(groups[0], groups[1])
    else:
        return merge(solve(groups, i - 1), groups[i])


"""
test cases
"""
# print(merge([10, 15, 30], [12, 15, 20]))
# print(merge([10, 12, 15, 15, 20, 30], [17, 20, 32]))
# print(sorted([10, 15, 30, 12, 15, 20, 17, 20, 32]))
given = [10, 15, 30], [12, 15, 20], [17, 20, 32]
given01 = [[3], [1, 2]]
given02 = [[1], []]
given03 = []

print(solve(given, len(given) - 1))
print(solve(given01, len(given01) - 1))
print(solve(given02, len(given02) - 1))
print(solve(given03, len(given03) - 1))
