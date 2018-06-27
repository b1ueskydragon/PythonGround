import re

r = re.compile("(\[)([0-9]+)(\])")
POS = 4
IDPOS = 1
PATH = ""


def read_file():
    file = open(PATH, 'r', encoding='UTF-8')

    for line in file:
        if line is '\n':
            continue
        id = line.split(' ')[POS]

        print(r.match(id).groups()[IDPOS])

    file.close()


read_file()

# sample
# r = re.compile("([a-zA-Z]+)([0-9]+)")
# strings = ['foofo21', 'bar432', 'foobar12345']
# print([r.match(string).groups() for string in strings])
