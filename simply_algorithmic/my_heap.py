import random


def heapsort(ary):
    """
    O(N) time to build a max heap,

    O(logN) time with (N - 1) calls
    to heapify all of the items in the heap
    except for the root node.

    :param ary: an array before heapify
    :return: sorted array
    """
    build_max_heap(ary)
    last = len(ary) - 1

    while last > 0:
        ary[0], ary[last] = ary[last], ary[0]
        heapify(ary, 0, last)
        last -= 1

    return ary


def heappop_max(heap):
    """
    Pop the largest item off the heap and re-heapify.
    """
    last = heap.pop()
    if heap:
        head = heap[0]
        heap[0] = last
        heapify(heap, 0, len(heap))  # start from root-position
        return head
    return last


def build_max_heap(ary):
    """
    Array to heap, in-place.

    O(N) time
    """
    for i in reversed(range(len(ary) // 2)):
        heapify(ary, i, len(ary))


def heapify(ary, i, endpos):
    """
    A node that has a child(ren), is same or larger than it's child(ren).
      - Add a child, left to right.
      - recursive and in-place.

    :param ary: array
    :param i: an index of current pos
    :param endpos: a maximum index of heap array
    """

    parent = i  # assume that current pos is a parent pos
    leftchild = 2 * i + 1  # leftmost child position
    rightchild = leftchild + 1

    if leftchild < endpos and ary[leftchild] > ary[i]:
        ''' left child is bigger than parent '''
        parent = leftchild

    if rightchild < endpos and ary[rightchild] > ary[parent]:
        ''' right child is bigger than left child, also parent '''
        parent = rightchild

    if parent != i:
        ary[i], ary[parent] = ary[parent], ary[i]
        heapify(ary, parent, endpos)


"""
ary = [8, 11, 9, 2, 10, 16]
build_max_heap(ary) 

# [16, 11, 9, 2, 10, 8]

       16
    11     9
  2  10     8

"""

ary = list(range(200_000))
random.shuffle(ary)
assert sorted(ary) == heapsort(ary)
