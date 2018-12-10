"""
- A node that has a child(ren), is same or larger than it's child(ren).
- Add a child, left to right.
"""


def heapify(ary):
    """
    array to heap, in-place.

    O(N) time
    """
    for i in reversed(range(len(ary) // 2)):
        _heapify(ary, i)


def _heapify(ary, i):
    """
    helper method of heapify. recursive.

    :param ary: array
    :param i: index
    """

    largest = i  # assume that parent's index is an largest index.
    left = 2 * i + 1  # leftmost child position
    right = left + 1

    if left < len(ary) and ary[left] > ary[i]:
        ''' left child is bigger than parent '''
        largest = left

    if right < len(ary) and ary[right] > ary[largest]:
        ''' right child is bigger than left child, also parent '''
        largest = right

    if largest != i:
        ary[i], ary[largest] = ary[largest], ary[i]
        _heapify(ary, largest)


def heappop_max(heap):
    """
    Pop the largest item off the heap and re-heapify.
    """
    last = heap.pop()
    if heap:
        head = heap[0]
        heap[0] = last
        _heapify(heap, 0)  # start from root-position
        return head
    return last


ary = [8, 11, 9, 2, 10, 16]
heapify(ary)

"""
       16
    11     9
  2  10     8

"""
print(ary)  # [16, 11, 9, 2, 10, 8]
print(heappop_max(ary))  # 16
print(ary)  # [11, 10, 9, 2, 8]
print(heappop_max(ary))  # 11
print(ary)  # [10, 8, 9, 2]
