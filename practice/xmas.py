import re

xmas = 'Merry-Christmas'
pattern = r"[a-zA-Z ]"


def mixed(target):
    list = []
    for i in range(len(target)):
        if re.match(pattern, target[i]):
            list.append(ord(target[i]))

    return list


print(mixed(xmas))


print(''.join(list(map(lambda s: chr(s), [77, 101, 114, 114, 121, 67, 104, 114, 105, 115, 116, 109, 97, 115]))))