def heappop_max(heap):
    """
    Pop the largest item off the heap and re-heapify.
    """
    last = heap.pop()
    if heap:
        head = heap[0]
        heap[0] = last
        heapify(heap, 0)  # start from root-position
        return head
    return last


def build_max_heap(ary):
    """
    Array to heap, in-place.

    O(N) time
    """
    for i in reversed(range(len(ary) // 2)):
        heapify(ary, i)


def heapify(ary, i):
    """
    A node that has a child(ren), is same or larger than it's child(ren).
      - Add a child, left to right.
      - recursive and in-place.

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
        heapify(ary, largest)


"""
ary = [8, 11, 9, 2, 10, 16]
build_max_heap(ary) 

# [16, 11, 9, 2, 10, 8]

       16
    11     9
  2  10     8

"""
