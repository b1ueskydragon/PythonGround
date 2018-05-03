'''
或る数nが素数であるかの判定は、
2～n－1の全ての自然数の中にnを割り切れる素数があるか調べれば確実に分かる。
'''
n = 10001

# nは作りたい素数の個数
def find_prime_num(n):
    prime_list = [2]
    i = 3
    while len(prime_list) < n:
        for j in prime_list:
            if i % j == 0:  # 素数以外の自然数は、複数の素数の積となり、合成数と呼ばれる
                break
        else:  # else文(の記述があった場合)のブロックは一度実行された後でfor文全体が終了
            prime_list += [i]
        i += 2  # 最初から奇数と絞る(素数は全て奇数)
    return prime_list


prime_list = find_prime_num(n)
result = prime_list[-1]
print(result)
