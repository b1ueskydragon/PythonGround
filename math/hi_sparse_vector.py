import sys

import scipy.sparse as sp


def gen_basic():
    """
    X.todense()
        : a dense matrix representation of this matrix.
            [[0. 1. 2.]
             [0. 0. 3.]
             [4. 5. 0.]]

    :return: Compressed Sparse Row format (not a dense matrix)
    """
    A = sp.lil_matrix((3, 3))
    A[0, 1] = 1.
    A[0, 2] = 2.
    A[1, 2] = 3.
    A[2, 0] = 4.
    A[2, 1] = 5.

    B = A.tocsr()  # convert this matrix to Compressed Sparse Row format; default is copy=false.
    return B  # not a dense matrix.


def print_vectors(X):
    """ just print out """

    """
    (0, 1)	1.0
    (0, 2)	2.0
    (1, 2)	3.0
    (2, 0)	4.0
    (2, 1)	5.0
    (0, 1)	1.0
    (0, 2)	2.0
    """
    print(X)

    """
    right: row num m (count from zero).
    left:  indices where the values are.
    
    (0, 0)	4.0
    (0, 1)	5.0
    """
    m = 2
    print(X[m])


def print_inner_structures(X):
    """ just print out """

    """ 
    a compressed list of non-zero elements. 
    [1. 2. 3. 4. 5.] 
    """
    print(X.data)

    """ 
    an indices of column that where `X.data` is. count in row direction. 
    [1 2 2 0 1]
    """
    print(X.indices)

    """ 
    an indices of boundary.
    [0 2 3 5]
    
    boundary       index of X.indices   value of X.indices
         r0   0    -                    -
    0 <= r1 < 2    0, 1                 1, 2 
    2 <= r2 < 3    2                    2
    3 <= r3 < 5    3, 4                 0, 1
    """
    print(X.indptr)


if __name__ == '__main__':
    X = gen_basic()

    print_vectors(X)

    print_inner_structures(X)

    sys.exit(0)
