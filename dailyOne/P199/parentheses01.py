def find_balance(given):
    left, right = "(", ")"
    given, last = list(given), len(given) - 1
    count = 0

    # head'(' and last')' are be required anyway (maybe).
    if given[0] is not left:
        given.insert(0, left)
        last += 1
        count += 1
    if given[last] is not right:
        last += 1
        given.insert(last, right)
        count += 1

    for i, p in enumerate(given):
        if i is last:
            break

        if p is given[i + 1]:
            given[i] = ''
            count += 1

    return ''.join(given), count


print(find_balance(input()))
