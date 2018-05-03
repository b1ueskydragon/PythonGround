# 500個以上の約数をもつ最初の三角数を求めて表示するプログラム
# ２番目の関数がnの増加によりとてもとても遅くなるので改良がとても必要

def a_tri_num(n):
    return int(n * (n + 1) / 2)


def divisor(n):
    target = a_tri_num(n)
    count = 0
    divisor_list = []
    for i in range(1, target * 2):
        if (target % i) == 0:
            divisor_list += [i]
        else:
            continue
    return divisor_list


def find_len():
    n = 1
    while len(divisor(n)) < 500:
        n += 1
        print(n)
    else:
        return a_tri_num(n)


print(find_len())
