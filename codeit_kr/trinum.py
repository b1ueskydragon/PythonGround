'''
繰り返しではなく、再帰で三角数
'''

def triangle_number(n):
    if n == 1: #base case
        return 1
    return triangle_number(n - 1) + n #recursive case

for i in range(1, 11):
    print(triangle_number(i))