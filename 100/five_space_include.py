'''
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
'''

# スペースも含むらしぃ

def five(stc):
    word_list = stc.replace(" ", ": :").split(":")
    word_bi_gram = []
    for i in range(len(word_list)):
        if i is 0:
            i = 0
        else:
            word_bi_gram.append(word_list[i - 1] + word_list[i])

    return word_bi_gram


def five_(stc):
    word_list = stc
    char_bi_gram = []
    for i in range(len(word_list)):
        if i is 0:
            i = 0
        else:
            char_bi_gram.append(word_list[i - 1] + word_list[i])

    return char_bi_gram

stc = "I am an NLPer"
print(five(stc))  # 単語 bi-gram
print(five_(stc))  # 文字 sbi-gram
