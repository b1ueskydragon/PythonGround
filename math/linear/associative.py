"""
Q: p.08 (10)

(AB)C == AB(C)

A(n,m) idx of elem (i,j)
B(m,l) idx of elem (j,k)
C(l,p) idx of elem (k,h)
"""

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

C = [
    [1, 2, 3]
]


def calc(matrix1, matrix2):
    res = [0 for _ in range(len(matrix1) * len(matrix2[0]))]
    pivot = len(res) // 2
    cnt = 0

    for i, a in enumerate(matrix1):
        for j, b in enumerate(matrix2):
            cnt += 1
            if cnt <= len(matrix2):
                # TODO loop
                res[0] += a[j] * b[0]
                res[1] += a[j] * b[1]
            else:
                res[2] += a[j] * b[0]
                res[3] += a[j] * b[1]

    return res  # TODO make not flatted


print(calc(A, B))

