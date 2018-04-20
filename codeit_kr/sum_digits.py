# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    if int(n) < 10:  # 一桁数字
        return n  # base case

    else:  # 長いのはここから書いていけばok...
        la = str(n)[len(str(n)) - 1]  # 最終桁(分解できない)
        n = str(n)[:len(str(n)) - 1]
        return int(sum_digits(n)) + int(la)  # recursive case  sum_digits(n) + n

# 테스트
print(type(sum_digits(1)))
print(sum_digits(1))
print(sum_digits(10))
print(sum_digits(22541))  # sum_digits(22541) + 1  -> sum_digits(225) + 4 + 1 ...
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))


# more simply ...
def sum_digits(n):
    if n < 10:
        return n
    else:
        str_n = str(n)
        return int(str_n[0]) + sum_digits(int(str_n[1:]))

print(sum_digits(12345))
