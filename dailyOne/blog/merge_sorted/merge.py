k = 3  # k sorted lists
n = 3  # each with size n


def merge(left, right):
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


# given = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
# print(merge(given))
print(list(merge([10, 15, 30], [12, 15, 20])))
print(list(merge([10, 12, 15, 15, 20, 30], [17, 20, 32])))
