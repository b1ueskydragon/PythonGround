import time


# リスト化
def num_to_list(num):
    return list(str(num))


# リスト化した num は奇数か？
def isOdd(list_num):
    return len(list_num) % 2 != 0


# 回文数ですか?
def is_palindrom(list):
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


def csv_to_num(csv_target):
    return csv_target.split(",")


# left から right までの回文数を求める
def find_all(csv_target):
    left = int(csv_to_num(csv_target)[0])
    right = int(csv_to_num(csv_target)[1])
    result = []
    target = left  # 出発
    while target <= right:
        target_list = num_to_list(target)
        if is_palindrom(target_list): result += [target]
        target += 1
    return result


# 探索
def find_center(result):
    ln = len(result)
    try:
        ctr = result[int(ln / 2)]
    except IndexError:
        return "-"

    if ln % 2 == 0:
        return ",".join([str(result[int(ln / 2) - 1]), str(ctr)])
    else:
        return ctr

START = int(round(time.time()))
print(find_center(find_all(input())))
END = int(round(time.time()))
print(END - START)
