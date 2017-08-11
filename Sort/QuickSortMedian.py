# 200000000ずつファイル読み込み
def read_file(num_range):
    open_path = path + "sort_median.txt"
    num_list = []
    file = open(open_path, "r", encoding="UTF-8")

    for num in file:
        num = int(num)

        if num_range <= num < (num_range + 200000000):
            num_list += [num]

    file.close()
    return num_list


# クイックソート
def quick_sort(list, left, right):
    cursor_left = left
    cursor_right = right
    center = list[int((cursor_left + cursor_right) / 2)]

    while True:
        while list[cursor_left] < center: cursor_left += 1
        while list[cursor_right] > center: cursor_right -= 1
        if cursor_left <= cursor_right:
            list[cursor_left], list[cursor_right] = list[cursor_right], list[cursor_left]
            cursor_left += 1
            cursor_right -= 1
        if cursor_left > cursor_right:
            break

    if left < cursor_right: quick_sort(list, left, cursor_right)
    if cursor_left < right: quick_sort(list, cursor_left, right)


# 書き出し
def write_file(list):
    write_path = path + "sort_median_result.txt"
    file = open(write_path, 'a', encoding="UTF-8")
    for el in list:
        el = str(el) + "\n"
        file.write(el)
    else:
        file.close()


# ソート検査機
def isSorted(list):
    i = 0
    while list[i] <= list[i + 1]:
        i += 1
        if i == len(list) - 1:
            return print("ok! sorted")
    else:
        return print("index [", i, "] and [", i + 1, "] are not sorted")


path = "/Users/jang_inhwa/Desktop/"  # pathは適宜変えること
num_range = 0
while num_range < (200000000 * 10):
    list = read_file(num_range)  # ソート前
    quick_sort(list, 0, len(list) - 1)  # ソート中

    write_file(list)
    list = []  # メモリ解放
   # if isSorted(list):  # 正しい場合書き出す
   #     write_file(list)
    num_range += 200000000
