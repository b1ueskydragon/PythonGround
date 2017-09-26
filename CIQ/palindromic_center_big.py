"""
GOAL = 真ん中の回文数
今回は、真ん中から探していく

真ん中周辺を探す?
"""

'''

52779812949
52779797725,52779897725
'''

# 材料
left = 28228056190
right = 77331569708
center = int((left + right) / 2)

print(center) # TODO さらに半分にわける

# 回文数ですか?
def is_palindrom(target):
    return int(target) == int(str(target)[::-1])


def binary_search(left, right):
    center = int((left + right) / 2)