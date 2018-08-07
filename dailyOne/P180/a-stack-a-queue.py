def interleave_half(stack):
    """
    interleave the first half of the stack(LIFO) with the second half reversed.
    - using only one other queue(FIFO)
    - in-place
    - Hint: Try working backwards from the end state.
      e.g) S[1,5,2,4] Q[3]   -1 th
           S[1,5] Q[2,4,3]   -2 th
    """
    queue = []
    size = len(stack)

    for _ in range(1, size):
        queue = list(reversed(stack[_:]))
        stack = stack[:_]
        stack += queue

    return stack, queue


given_odd = [1, 2, 3, 4, 5]
given_even = [1, 2, 3, 4]

print(interleave_half(given_odd))
print(interleave_half(given_even))
