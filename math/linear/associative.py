import numpy as np

"""
Q: p.08 (10)

(AB)C == AB(C)

A(n,m) idx of elem (i,j)
B(m,l) idx of elem (j,k)
C(l,p) idx of elem (k,h)
"""

# (2 x 3)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# (3 x 2)
B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# (2 x 1)
C = [
    [10],
    [11]
]


# A(BC) = (2 x 3) x (3 x 1)
# (AB)C = (2 x 2) x (2 x 1)


def calc1(matrix1, matrix2):
    res = []
    inner = [0 for _ in range(len(matrix1) * len(matrix2[0]))]
    cnt = 0

    for i, a in enumerate(matrix1):
        for j, b in enumerate(matrix2):
            cnt += 1
            if cnt <= len(matrix2):
                # TODO Generalization with loop
                inner[0] += a[j] * b[0]
                inner[1] += a[j] * b[1]
            else:
                inner[2] += a[j] * b[0]
                inner[3] += a[j] * b[1]

    res.append([inner[0], inner[1]])
    res.append([inner[2], inner[3]])

    return res


def calc2(matrix1, matrix2):
    res = []
    inner = [0 for _ in range(len(matrix1) * len(matrix2[0]))]

    for i, a in enumerate(matrix1):
        for j, b in enumerate(matrix2):
            inner[i] += a[j] * b[0]
        res.append([inner[i]])

    return res


AB = calc1(A, B)  # (2 x 2)
BC = calc2(B, C)  # (3 x 1)
print(AB)
print(BC)
