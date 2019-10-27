# input
alphas = [chr(i) for i in range(97, 123)]
nums = [10 * i for i in range(1, 10)]


def pick3th(xs):
    pos = 2
    while xs and pos < len(xs):
        print(xs.pop(pos))
        pos += 2
        if pos >= len(xs):
            pos -= len(xs)  # revert
    while xs:
        print(xs.pop(0))


pick3th(nums)
print(nums)
pick3th(alphas)
print(alphas)
