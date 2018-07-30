"""
AP 2012 A 2
実際の問題では idx が 1 はじまりだが, ここでは 0 はじまりとする.
"""

# TODO Change String to Boolean overall.

"""
init
"""
N = 8
col = ['free' for _ in range(0, N)]  # size N
upwd = ['free' for _ in range(0, 2 * N - 1)]  # size N+(N-1)
downwd = ['free' for _ in range(0, 2 * N - 1)]  # size N+(N-1)
pos = [0 for _ in range(0, N)]  # その行に配置したクイーンの位置(列番号 - 横から数える番号)を記録


def search(i):
    """
    search col[0] to col[N-1]
        - General terms (origin)
            * upwd[i+k-1]
            * downwd[i+N-k]

    :param i: column (行 - なので, 上から下へ探索)
    :return:
    """
    for k in range(0, N):
        if col[k] is 'free' and upwd[i + k - 1] is 'free' and downwd[i + N - 1 - k] is 'free':
            pos[i] = k
            col[k] = 'not_free'
            upwd[i + k - 1] = 'not_free'
            downwd[i + N - 1 - k] = 'not_free'
            if i is N - 1:  # 最後に到達したか(無事全行に配置が終わったか)
                return 'success'
            else:
                if search(i + 1) is 'success':
                    return 'success'
                else:
                    pos[i] = 0
                    col[k] = 'free'
                    upwd[i + k - 1] = 'free'
                    downwd[i + N - 1 - k] = 'free'
    return 'failure'


print(search(0))
print(upwd)
print(downwd)
print(pos)
