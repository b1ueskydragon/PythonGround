import re

def bigram_word(words):
  result_list = []
  for i in range(len(words)-1):
    result_list.append(words[i] + words[i+1])
  return result_list

def bigram_char(chars):
  result_list = []
  for i in range(len(chars)-1):
    result_list.append(chars[i] + chars[i+1])
  return result_list

msg="I am an NLPer"
words = re.split('\W+', msg)

print(bigram_word(words))
chars = msg.replace(" ","")
print(bigram_char(chars))


def bigram(mojiarr, joinword):
    length = len(mojiarr)
    if length < 2:
        return None

    ret = []
    for idx in range(length):
        if idx + 1 < length:
            ret.append(mojiarr[idx] + joinword + mojiarr[idx + 1])
    return ret

def char_bigram(mojiarr):
    return bigram(mojiarr.replace(" ",""), "")

def word_bigram(mojiarr):
    return bigram(mojiarr.split(" "), " ")

mojiretu = "I am an NLPer"
print("元の文字")
print(mojiretu)
print("文字バイグラム")
print(char_bigram(mojiretu))
print("単語バイグラム")
print(word_bigram(mojiretu))


t="I am an NLPer"

l1=iter(t.split())  # 改行コードと space がデフォルト
l2=iter(t.split())  # 一個ずらし
next(l2)
print(list(zip(l1,l2)))

l1=iter(t)
l2=iter(t)
next(l2)
print(list(zip(l1,l2)))
