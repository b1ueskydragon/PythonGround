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