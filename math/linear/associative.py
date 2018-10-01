"""
Q: p.08 (10)

(AB)C == AB(C)

A(n,m) idx of elem (i,j)
B(m,l) idx of elem (j,k)
C(l,p) idx of elem (k,h)
"""


# TODO with numpy
def sum(i, h, m, l):
    for j in range(1, m + 1):
        for k in range(1, l + 1):
            print(i, j, k, h)


sum('i', 'h', 3, 5)
