# ジェネレータ.状態を保持する. 関数よりインスタンスに近い
# List 生成分のメモリが節約される
def x():
    a = 0
    while True:
        yield a
        a += 1


# イテレートの状態が保持されている変数 (next() で取り出し可能)
rst = x()

for i in rst:
    print(i)
    if i == 9:
        break


# next() で実装
def gene(a=0):
    b = a
    while True:
        b = b + 1
        yield b


if __name__ == "__main__":
    g = gene(1)
    print(next(g))
    print(next(g))
    print(next(g))
