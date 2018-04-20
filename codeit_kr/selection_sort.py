'''
def test(list):

    for i in range(len(list)):
        print(list[i:])

list = [1, 2, 3, 4, 5]
test(list)
'''


# 選択ソート(value)
def selection_sort(my_list):

    for i in range(len(my_list)):
        min = my_list[i]

        for j in range(i + 1, len(my_list)):
            if (my_list[j] < min):
                min = my_list[j]
                my_list[i], my_list[j] = my_list[j], my_list[i]  # i, j, minのscopeが異なるからインデント注意

some_list = [11, 3, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)


# 選択ソート(index)
def selection_sort(my_list):
    for i in range(len(my_list)):
        min_idx = i

        for j in range(i + 1, len(my_list)):
            value = my_list[j]
            if (value < my_list[min_idx]):
                min_idx = j

        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i] #最小値を探し終わってから交換(上記より少ない交換数)

some_list = [11, 3, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)