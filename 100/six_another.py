'''
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ,
 XとYとして求め，XとYの和集合，積集合，差集合を求めよ.
 さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''


def bigram(stc):
    word_list = []
    char_bi_gram = []

    for i in stc:
        if i is not " ":
            word_list += i

    for i in range(len(word_list)):
        if i is 0:
            i = 0
        else:
            el = word_list[i - 1] + word_list[i]  # 集合なので重複除去
            if el not in char_bi_gram:
                char_bi_gram.append(el)

    return char_bi_gram


X = bigram("paraparaparadise")
Y = bigram("paragraph")

print(X, "集合 X")
print(Y, "集合 Y")


# 和集合
def __OR__(X, Y):
    result = []
    result.extend(X)  # グローバルな X を直接いじらないバージョン
    for y in Y:
        if y not in X:
            result.append(y)
    return result
print(__OR__(X, Y), "和集合")


# 積集合
def __AND__(X, Y):
    result = []
    for y in Y:
        if y in X:
            result.append(y)
    return result
print(__AND__(X, Y), "積集合")


# 差集合 ( Y - __AND__(X, Y) )
def __SETDIFF__(X, Y):
    result = []
    for y in Y:
        if y not in __AND__(X, Y):
            result.append(y)
    return result
print(__SETDIFF__(X, Y), "差集合")


# 'se'というbi-gramがXおよびYに含まれるか
print("has'se' -> ", (lambda target, target_list: target in target_list)('se', __OR__(X, Y)))
