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
    # print(pairs)

    i, j = 0, 1
    while i < N and j < N:
        curr_dis = pairs[j][1] - pairs[i][1]
        if curr_dis >= dis:
            dis = curr_dis
            curr = max(curr, abs(pairs[j][0] - pairs[i][0]))
        elif curr_dis == 0:  # TODO: fix here
            curr = curr - pairs[i][0] + pairs[j][0]

        i += 1
        j += 1

    return (curr, -1)[curr == 0]  # no adjacent indices exist


if __name__ == '__main__':
    print(solution(A=[1, 4, 7, 3, 3, 5]))  # 4
    print(solution(A=[0, 3, 3, 7, 5, 3, 11, 1]))  # 7
