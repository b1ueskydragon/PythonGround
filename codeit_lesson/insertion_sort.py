# 挿入ソート
def insertion_sort(my_list):
    for i in range(len(my_list)):  # 挿入対象の探索
        tmp = my_list[i]
        if i > 0:
            j = i - 1
            target = my_list[j]
            while j != 0 and tmp > target:
                j -= 1
            my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list

some_list = [11, 3, 6, 4, 12, 1, 2]
print(insertion_sort(some_list))
