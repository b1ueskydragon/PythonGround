'''
GOAL = 真ん中の回文数

52779812949
52779797725,52779897725
'''


mill = 10_000

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
    result = []
    target = left  # 出発
    while target <= right:
        if is_palindrom(target): result += [target]
        target += 1
    return result

# 材料
left = 1000000000
right = 9000000000
center = int((left + right) / 2)
new_center = binary_search(left, right)

print(find_all(left, new_center))
print(find_all(new_center, new_center))