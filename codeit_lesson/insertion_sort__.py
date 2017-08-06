def insertion_sort(list):
    for i in range(len(list)):
        key = list[i]

        # i - 1 からスタート、左方向に一つずつ探索
        # 左の端([0])まで探索し終えたか、
        # key の入る場所が見つかったら終了

        j = i - 1  # 必ず i よりは左で (そして0よりは同じか大きい)

        while j >= 0 and list[j] > key:  # 交換し続ける条件
            list[j + 1] = list[j]
            j -= 1  # さらに左へ移動

        # while の外
        # key が入る場所に挿入
        # 左の端に到着して、j が -1 なら [0] に key を挿入
        list[j + 1] = key

some_list = [11, 3, 6, 4, 4, 12, 1, 2, 3]
insertion_sort(some_list)
print(some_list)