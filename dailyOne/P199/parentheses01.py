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

    # TODO minimum count ?
    for i, p in enumerate(given):
        if i is last:
            break

        if p is right and given[i + 1] is right:
            given[i] = ''
            count += 1
        if p is left and given[i + 1] is left:
            given[i + 1] = right
            count += 1

    return ''.join(given), count


parentheses00 = "(()"
parentheses01 = "))()("
parentheses02 = "(((("
parentheses03 = "((((()()((())))((()()()()()())))))))(("

print(find_balance(parentheses00))  # "(())"  "()"  "()()"
print(find_balance(parentheses01))  # "()()"  "()()()()"
print(find_balance(parentheses02))
print(find_balance(parentheses03))
