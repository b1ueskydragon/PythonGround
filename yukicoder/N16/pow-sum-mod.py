def exps_input(exps):
    return [int(e) for e in exps.split(' ')]


mod = 1_000_003


def pow_2(x, y):
    K = 1
    while y > 1:
        if y % 2 == 0:
            x = x ** 2 % mod
            y = y // 2
        else:
            K = K * x % mod
            x = x ** 2 % mod
            y = (y - 1) // 2
    return K * x % mod


sum = 0
base = int(input().split(' ')[0])
for exp in exps_input(input()):
    sum += pow_2(base, exp)

print(sum % mod)
