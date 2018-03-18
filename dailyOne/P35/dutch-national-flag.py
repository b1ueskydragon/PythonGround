def partition_basic(arr):
    """
    [[演習]]

    RとR以外、要素が二つだけとみなして着目する

    :param arr:
    :return:
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        if arr[low] == 'R':
            low += 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
            high -= 1

    return arr


arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(partition_basic(arr))


def partition(ary):
    """
    [[本番]]

    R のいるべき場所 [0]~[low]
    G のいるべき場所 [low]~[mid]
    B のいるべき場所 [mid]~[high]

    真ん中(index of G)に着目して三つのインデックスで配列を操作する

    :param ary:
    :return:
    """

    low, mid, high = 0, 0, len(ary) - 1

    while mid <= high:
        if ary[mid] == 'R':
            ary[low], ary[mid] = ary[mid], ary[low]
            low += 1
            mid += 1
        elif ary[mid] == 'G':
            mid += 1
        else:
            ary[mid], ary[high] = ary[high], ary[mid]
            high -= 1  # swapしてきたのが'G'でない可能性もあるのでmidの着目はそのまま.

    return ary


ary = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(partition(ary))
