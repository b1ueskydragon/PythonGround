# 자리수 합 리턴
def sum_digit(num):
    num = str(num)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum

sum = 0
for i in range(1001):
    sum += sum_digit(i)
print(sum)
