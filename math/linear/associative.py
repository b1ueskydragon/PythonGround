import numpy as np

"""
Q: p.08 (10)

(AB)C == AB(C)

A(n,m) idx of elem (i,j)
B(m,l) idx of elem (j,k)
C(l,p) idx of elem (k,h)
"""

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

C = np.array([
    [1, 2, 3]
])


def res(matrix1, matrix2):
    sum1, sum2, sum3, sum4 = [], [], [], []

    for i, a in enumerate(matrix1):
        for j, b in enumerate(matrix2):
            if len(sum1) < 3:
                sum1.append(a[j] * b[0])
                sum2.append(a[j] * b[1])
            else:
                sum3.append(a[j] * b[0])
                sum4.append(a[j] * b[1])

    return np.array([
        [sum(sum1), sum(sum2)],
        [sum(sum3), sum(sum4)]
    ])


print(res(A, B))
