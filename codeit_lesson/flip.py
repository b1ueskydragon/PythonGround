# case 1 (ijrd1)
def flip(fst_idx, lst_idx, some_list):
    if lst_idx <= fst_idx:  # base case
        return some_list
    else:  # recursive case
        some_list[fst_idx], some_list[lst_idx] = some_list[lst_idx], some_list[fst_idx]
        fst_idx += 1
        lst_idx -= 1
    return flip(fst_idx, lst_idx, some_list)

# Test
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flip(0, len(some_list) - 1, some_list))



'''
def flip(some_list):
    if len(some_list) <= 2:  # base case
        return some_list
    else:  # recursive case
        lst_idx = len(some_list) - 1
        some_list[0], some_list[lst_idx] = some_list[lst_idx], some_list[0]
        print(some_list)
        some_list = some_list[1:lst_idx]
    return flip(some_list)


# Test
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
'''