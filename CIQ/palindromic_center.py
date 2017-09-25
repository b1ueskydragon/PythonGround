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


'''
# 自然数でない場合の例外
class NotNaturalError(Exception):
    def message(self):
        print("should be Natural number")
'''


# left から right までの回文数を求める
def find_all(csv_target):
    left = int(csv_to_num(csv_target)[0])
    right = int(csv_to_num(csv_target)[1])
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
        return ",".join([str(result[int(ln / 2) - 1]), str(ctr)])
    else:
        return ctr


def csv_to_num(csv_target):
    return csv_target.split(",")


print(find_center(find_all(input())))

'''
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
'''


'''
試したいアルゴリズム（大きい桁対策)
①普通に左から右へ探索
②center 軸から左右比較して false になったらストップ
③それか再帰で生成（？）多きすぎる数字は最初から文字列として処理すべき？
'''