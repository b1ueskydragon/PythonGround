def solve(a, b):
    print(''.join([a[i] + b[i] for i in range(min(len(a), len(b)))]))


pat = "パトカー"
tax = "タクシー"
solve(pat, tax)
