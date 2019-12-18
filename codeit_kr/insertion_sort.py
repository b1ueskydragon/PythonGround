def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i + 1] = list[i]
                list[i] = value
                i -= 1
            else:
                break
    return list


some_list = [11, 3, 6, 4, 12, 1, 2]
print(insertion_sort(some_list))
