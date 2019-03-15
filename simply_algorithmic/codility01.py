"""
largest bi-valued slice in an array
"""


def solution(A):
    N = len(A)
    if N < 2:
        return 0
    if N == len(set(A)):
        return N

    l, r, curr = 0, 0, 0
    lookup = set()

    while l < N and r < N:
        lookup.add(A[l])
        if len(lookup) > 2:
            curr = max(curr, l - r)
            r = l - 1
            lookup = {A[l], A[r]}

        l += 1

    return max(curr, l - r)


print(solution(A=[0, 5, 4, 4, 5, 12]))  # (1, 4) 4
print(solution(A=[5, 4, 4, 5, 0, 12]))  # (0, 3) 4
print(solution(A=[0, 1]))  # (0, 1) 2
print(solution(A=list(range(100001))))  # (0, 100001) 100001
print(solution(A=[]))  # 0
print(solution(A=[0, 0, 0, 1, 1, 1, 1]))  # 7
