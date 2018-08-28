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


parentheses00 = "(()"
parentheses01 = "))()("
parentheses02 = "(((("
print(find_balance(parentheses00))  # "(())"  "()"
print(find_balance(parentheses01))  # "()()"  "()()()()"
print(find_balance(parentheses02))
