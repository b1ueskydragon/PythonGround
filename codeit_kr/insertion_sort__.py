def insertion_sort(list):
    for i in range(len(list)):
        key = list[i]

        j = i - 1

        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key


some_list = [11, 3, 6, 4, 4, 12, 1, 2, 3]
insertion_sort(some_list)
print(some_list)
