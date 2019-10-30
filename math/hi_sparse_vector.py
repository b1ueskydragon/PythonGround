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


if __name__ == '__main__':
    X = gen_basic()

    """ a compressed list of non-zero elements. [1. 2. 3. 4. 5.] """
    print(X.data)

    """ an indices of column that where `X.data` is. count in row direction. [1 2 2 0 1] """
    print(X.indices)

    # [0 2 3 5]
    print(X.indptr)

    sys.exit(0)
