def solve(lst, head=0):
    # jump to next head. not necessary remove elements.
    acc = 0
    for i, n in enumerate(lst):
        acc += n
        if acc == 0:
            lst = lst[i + 1:]

        elif acc == lst[head]:
            lst = [lst[head]] + lst[i + 1:]

    return lst


# linked list
given = [3, 4, -7, 5, -6, 6]
given00 = [5, -6, 6, 7]
given01 = [0, 4, -7, 7, 3, 8]
given02 = [4, -7, 7, 3, 8, -8, -8]

# print(solve(given))  # 5
print(solve(given00))  # 5
# print(solve(given01))  # 4, 3, 8
print(solve(given02))  # 4, 3, -8
