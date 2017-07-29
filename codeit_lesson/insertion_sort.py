# 삽입 정렬
def insertion_sort(my_list):
    for i in range(len(my_list)):
        my_list[i] < my_list[i + 1]


some_list = [11, 3, 6, 4, 12, 1, 2]
print(insertion_sort(some_list))