import re
pattern = r"[a-zA-Z ]"
repatter = re.compile(pattern)

basestr = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
wordsstr = "".join(repatter.findall(basestr))

first_char_i = [1, 5, 6, 7, 8, 9, 15, 16, 19]

result = {}

wordslist = re.split(" ", wordsstr)
for i, word in enumerate(wordslist):
    symbol = ""
    key = i + 1
    if key in first_char_i:
        symbol = word[0]
    else:
        symbol = word[0:2]
    result[key] = symbol
print(result)
