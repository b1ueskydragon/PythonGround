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

    return right_lst_reverse + left_lst_reverse


print(split_flip([10, 8, 5, 2, 0, 23, 3, 2, -1, 3, 5, 2, 11, 33]))

print('\n')


def is_palindrome(lst):
    if len(lst) < 2:
        return True
    else:
        return lst[:1] == lst[-1:] and is_palindrome(lst[1:-1])


print(is_palindrome([1, 2, 3, 2, 1]))
print(is_palindrome([int(x) for x in str(707675040576707)]))
