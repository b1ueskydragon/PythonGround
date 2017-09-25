


target = 10301
l = len(str(target))

new_target = str(target)[::-1]

if int(target) == int(new_target):
    print("a")


# 大きい桁テスト
big_num = 1000000000000000
one_small = 999999999999999

list_big_num = list(str(big_num))


print(type(list_big_num))


center = int(len(list_big_num)/2)

center_value = list_big_num[center]


# [center] から [0] へ


# [center] から [len -1] へ
