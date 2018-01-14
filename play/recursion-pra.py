#!/usr/bin/python
# -*- Coding: utf-8 -*-


def flip(lst):
    if len(lst) < 2:
        print(lst)
        print("あ")
        return lst
    else:
        print(lst)
        return flip(lst[1:]) + lst[:1]


# [1:] tail (type: list)
# [:1] head (type: list)


test = [1, 2, 3]
result = flip(test)
print(result)

print('\n')


def factorial(i):
    if i < 2:  # cannot split anymore (base-case)
        return i
    else:  # pattern (recursive-case)
        return i * factorial(i - 1)


# 5! = 5 * 4!, 4! = 4 * 3! ...
# basic case == 1


print(factorial(5))

print('\n')


def flip_recursion(lst):
    if len(lst) < 2:
        return lst
    else:
        return flip_recursion(lst[1:]) + lst[:1]


def split_flip(lst):
    ctr_idx = int(len(lst) / 2)

    left_lst = lst[:ctr_idx]
    left_lst_reverse = flip_recursion(left_lst)

    right_lst = lst[ctr_idx:]
    right_lst_reverse = flip_recursion(right_lst)

    head_left = left_lst_reverse[:1]
    head_right = right_lst_reverse[:1]

    if head_left > head_right:
        result = left_lst_reverse + right_lst_reverse
    else:
        result = right_lst_reverse + left_lst_reverse

    return result


print(split_flip([1, 2, 3, 4, 5]))
