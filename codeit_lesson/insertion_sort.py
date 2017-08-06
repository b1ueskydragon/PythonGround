# 挿入ソート
def insertion_sort(list):
    for index in range(1, len(list)):

        value = list[index]  # 比較対象の探索

        i = index - 1
        # compare value to each item to the left on it
        #  keep taking i further left, until i == beginning of the list (0)

        while i >= 0:
            if value < list[i]:
                list[i + 1] = list[i]  # shift number in slot i right to i+1
                list[i] = value  # shift value left into slot i

               # list[i], list[i+1] = list[i+1], list[i]  # にしても同じ結果ー。

                i -= 1  # need decremented i
            else:  # when don't need shift value anymore (already-right-placed)
                break

    return list

some_list = [11, 3, 6, 4, 12, 1, 2]
print(insertion_sort(some_list))
