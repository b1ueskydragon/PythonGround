'''
入力は
99,120
のようになっています。
下限と上限がコンマ区切りで並んでいます。

下限以上で、上限以下の回文数の真ん中の値を求めてください。

出力も普通に10進数です。
範囲内にある回文数が奇数個の場合には、中央の値はひとつに決まるのでそれを。

偶数個の場合にはぴったり中央の値はありませんので、
中央付近の2つの値をコンマ区切りで昇順に出力してください。

ただし、範囲内に回文数がひとつもない場合は
-
を出力してください。

0 < 下限 < 上限 ≦ 一千兆 です。
'''


# 自然数でない場合の例外
class NotNaturalError(Exception):
    def message(self):
        print("should be Natural number")


# left から right までの回文数を求める
def find_all(left, right):
    result = []
    target = left  # 出発
    while target <= right:
        if is_palindrom(target): result.append(target)
        target += 1
    return result


# 回文数ですか?
def is_palindrom(target):
    return int(target) == int(str(target)[::-1])


# 探索
def find_center(result):
    ln = len(result)
    try:
        ctr = result[int(ln / 2)]
    except IndexError:
        return "-"

    if ln % 2 == 0:
        return result[int(ln / 2) - 1], ctr
    else:
        return ctr


try:
    print("ここから:")
    left = int(input())
    print("ここまで:")
    right = int(input())

    if left <= 0 or right <= 0:
        raise NotNaturalError

    print(find_center(find_all(left, right)))

except ValueError:
    print("Please input a <class 'int'>.")
except NotNaturalError as e:
    e.message()
