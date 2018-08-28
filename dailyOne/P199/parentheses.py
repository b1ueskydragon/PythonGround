"""
Find the balanced string using the minimum number of insertions and deletions.
If there are multiple solutions, return any of them.

Given "(()", you could return "(())".
Given "))()(", you could return "()()()()".
"""


def find_balance(given):
    left, right = "(", ")"
    one = "()"
    ln, rn = 0, 0

    for p in given:
        if p is left:
            ln += 1
        else:
            rn += 1

    # TODO balance
    # TODO minimum
    # TODO deletions
    while ln > rn:
        given += right
        rn += 1
    while ln < rn:
        given += left
        ln += 1

    return given


def find_balance01(given):
    left, right = "(", ")"
    given, last = list(given), len(given) - 1

    # head'(' and last')' are be required anyway (maybe).
    if given[0] is not left:
        given.insert(0, left)
        last += 1
    if given[last] is not right:
        last += 1
        given.insert(last, right)

    # TODO minimum count ?
    for i, p in enumerate(given):
        if i is last:
            break

        if p is right and given[i + 1] is right:
            given[i] = ''
        if p is left and given[i + 1] is left:
            given[i + 1] = right

    return ''.join(given)


parentheses00 = "(()"
parentheses01 = "))()("
parentheses02 = "(((("
print(find_balance(parentheses00))  # "(())"  "()"  "()()"
print(find_balance(parentheses01))  # "()()"  "()()()()"
print(find_balance(parentheses02))  # "(((())))"
print()
print(find_balance01(parentheses00))  # "(())"  "()"  "()()"
print(find_balance01(parentheses01))  # "()()"  "()()()()"
print(find_balance01(parentheses02))
