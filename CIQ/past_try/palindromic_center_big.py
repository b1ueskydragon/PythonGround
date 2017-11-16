"""
GOAL = 真ん中の回文数
今回は、真ん中から探していく

真ん中周辺を探す?
"""

'''

52779812949
52779797725,52779897725
'''


# print(center) # TODO さらに半分にわける (基底caseは範囲が10_000になった時)


# 回文数ですか?
def is_palindrom(target):
    return int(target) == int(str(target)[::-1])


def binary_search(left, right):
    center = int((left + right) / 2)
    if (center - left) > 10000:
        center = binary_search(left, center)
    return center


# left から right までの回文数を求める
def find_all(left, right):
    #left = int(csv_to_num(csv_target)[0])
    #right = int(csv_to_num(csv_target)[1])
    result = []
    target = left  # 出発
    while target <= right:
        if is_palindrom(target): result += [target]
        target += 1
    return result


# 材料
left = 28228056190
right = 77331569708
center = int((left + right) / 2)
new_center = binary_search(left, right)

print(find_all(left, new_center))
print(find_all(new_center, new_center))

#  普通に 10_000ずつ分けて処理してよさそう