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
            char_bi_gram.append(word_list[i - 1] + word_list[i])

    return char_bi_gram


sample = "paraparaparadise"
sample_ = "paragraph"

X = bigram(sample)
Y = bigram(sample_)
print(X, "集合 X")
print(Y, "集合 Y")

print("")

# 和集合
def __OR__(X, Y):
    result = X
    for y in Y:
       if y not in X:
           result.append(y)
    return result

print(__OR__(X, Y), "和集合")


# 積集合
def __AND__(X, Y):
    result = X
    for y in Y:
        if y in X:
            result.append(y)
    return result

print(__AND__(X, Y), "積集合")


# 差集合
def __SETDIFF__(X, Y):
    result = []
    for x in X:
        if x not in Y:
            result.append(x)
    return result

print(__SETDIFF__(X, Y), "差集合")


# 'se'というbi-gramがXおよびYに含まれるか
