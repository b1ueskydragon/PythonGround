# 挿入ソート
def insertion_sort(my_list):
    for i in range(len(my_list)):
        target = my_list[i]
        cs = i + 1
        if target < my_list[cs]:
            my_list = my_list[cs:]
            cs += 1

some_list = [11, 3, 6, 4, 12, 1, 2]
print(insertion_sort(some_list))