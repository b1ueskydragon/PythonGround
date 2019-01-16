def solve(msg):
    for i in range(len(msg)):
        if i % 2 == 0:
            yield msg[i]


given = "パタトクカシーー"
print(''.join(list(solve(given))))
