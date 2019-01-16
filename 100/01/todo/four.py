'''
"Hi He Lied Because Boron Could Not Oxidize Fluorine.
 New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''

period = "."
space = " "
list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

def word_list(stc):
    stc = stc.split(space)
    rst = []
    for idx in range(len(stc)):
        if period in stc[idx]:
            stc[idx] = stc[idx].replace(period, "")
        rst += [stc[idx]]
    return rst


def quiz_4(word_list):
    dict = {}
    for idx in range(len(word_list)):
        num = idx + 1
        if num in list:
            dict[num] = word_list[idx][0]
        else:
            dict[num] = word_list[idx][0:2]
    return dict


target_stc = "Hi He Lied Because Boron Could Not Oxidize Fluorine." \
             " New Nations Might Also Sign Peace Security Clause. Arthur King Can."
print(quiz_4(word_list(target_stc)))

# Might .. Mi .. ? Mg ?
