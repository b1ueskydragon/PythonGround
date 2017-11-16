'''
target = 10301
l = len(str(target))

new_target = str(target)[::-1]

if int(target) == int(new_target):
    print("a")
'''


# リスト化
def num_to_list(num):
    return list(str(num))


# リスト化した num は奇数か？
def isOdd(list_num):
    return len(list_num) % 2 != 0


# refactoring
# [center] から [0] へ  VS  [center] から [len -1] へ
def find_and_move(list):
    # 奇数 len の場合
    if isOdd(list):
        center = int(len(list) / 2)
        left = center - 1
        right = center + 1
        for i in range(center):
            if list[left] == list[right]:
                left -= 1
                right += 1
                if (left < 0): return True
        else:
            return False

    if not isOdd(list):
        center = int(len(list) / 2) - 1
        left = center
        right = center + 1
        for i in range(center + 1):
            if list[left] == list[right]:
                left -= 1
                right += 1
                if (left < 0): return True
        else:
            return False


# 大きい桁テスト
big_num = 1000000000000000  # 奇数
one_small = 999999999999999  # 偶数
test_num = 11466666411  # 奇数
test_num_even = 300330033003  # 偶数

'''
target_list = num_to_list(big_num)
target_list_ = num_to_list(one_small)

print(isOdd(target_list))
print(isOdd(target_list_))
'''

# 奇数
target_list__ = num_to_list(test_num)
print(find_and_move(target_list__))

# 偶数
target_list___ = num_to_list(test_num_even)
print(find_and_move(target_list___))


# 大きいやつ
very_big_one = num_to_list(12345678900987654321)
print(find_and_move(very_big_one))
