"""
given a non empty array A consisting of N integers
returns a maximum distance between indices of this array
that have adjacent values
"""


# N = 40_000  # max N


def solution(A):
    N = len(A)
    pairs = list(zip(range(N), A))
    pairs.sort(key=lambda p: p[1])
    dis = 0  # distance
    curr = 0

    i, j = 0, 1
    while i < N and j < N:
        dis = max(dis, pairs[j][1] - pairs[i][1])
        curr = max(curr, abs(pairs[j][0] - pairs[i][0]))
        i += 1
        j += 1

    return (curr, -1)[curr == 0]  # no adjacent indices exist


if __name__ == '__main__':
    print(solution(A=[1, 4, 7, 3, 3, 5]))
    print(solution(A=[0, 3, 3, 7, 5, 3, 11, 1]))
