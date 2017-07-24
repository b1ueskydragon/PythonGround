#1000未満の自然数のうち、2または3の倍数のSUM

def multiple(N):
    r = 1
    sum = 0
    while r < N:
        if r % 2 == 0 or r % 3 == 0:
            sum += r
        r += 1
    return sum

print(multiple(1000)) # 333167