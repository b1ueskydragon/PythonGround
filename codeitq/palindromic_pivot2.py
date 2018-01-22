# 回文数の判定だけする
def is_pal(num):
    return str(num) == str(num)[::-1]


# 真ん中だけ求める
def center(a, b):
    return int((a + b) / 2)


result = []


# 探索だけする
def binary_search(start, end):
    if end - start == 1:
        if is_pal(start):
            print(start)  # どちらかの端しか入らない
    else:
        binary_search(start, center(start, end))
        binary_search(center(start, end), end)


binary_search(1900, 10001)
