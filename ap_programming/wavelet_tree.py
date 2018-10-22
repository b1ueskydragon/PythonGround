"""
AP 2018 A 3
"""

""" 文字 : 符号 のペア. C : 01 の場合, 0がキー, 1がキーの値 """
codes: dict = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}


def convert(string):
    """ Convert string to code. """
    res = []
    for c in string:
        if c in codes:
            res.append(codes[c])
    return ''.join(res)


def extract_key(code):
    return ''.join([code[i] for i in range(len(code)) if i % 2 == 0])


"""
image>
         CTCGAGAGTA
        /          \
    CCAAA         TGGGT
    /   \         /   \
  AAA   CC      GGG   TT

"""


class Node:
    def __init__(self, key=None):
        self.key = int(key)
        self.left = None
        self.right = None

    def add(self, key):
        key = int(key)
        if key <= self.key:
            if not self.left:
                self.left = Node(key)
            else:
                self.left.add(key)
        else:
            if not self.right:
                self.right = Node(key)
            else:
                self.right.add(key)


class WaveletMatrix:
    def __init__(self):
        self.root = None

    def add(self, key_string):
        """
        TODO

        キー値のビット列を左から1ビットずつ順番に見ていき, キー値の元になった文字列から
        そのビットに対応する文字を, ビットの値が0の場合(左)とビットの値が1の場合(右)とで分けて取り出し
        それぞれの文字を順番に並べて新たな文字列を作成する.

        取り出した文字列の中の文字が2種類以上の場合は, その文字列に対応する新たなノードを生成し,
        左(または右)の子ノードにする.

        1種類の場合は, 子ノードは生成せず, 処理を終了する.
        """
        for key in key_string:
            if not self.root:
                self.root = Node(key_string)
            else:
                self.root.add(key)


target = "CTCGAGAGTA"
code = convert(target)
key_string = extract_key(code)
print(code)
print(key_string)

tree = WaveletMatrix()
tree.add(key_string)

tree  # for Debug
