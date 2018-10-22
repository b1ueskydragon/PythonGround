"""
AP 2018 A 3
"""

"""
文字 : 符号 のペア. 

C : 01 の場合, 
C に該当する符号 01 の 0がキー, 1がキーの値 
"""
code_map: dict = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}


def convert(string):
    """ Convert string to code. """
    res = []
    for c in string:
        if c in code_map:
            res.append(code_map[c])
    return res


# TODO revert code to string if needed.

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
    def __init__(self, codes=None):
        self.codes = codes
        self.left = None
        self.right = None

    def add(self, codes):
        cache_left, tmp_right = [], []

        for code in codes:
            # ビットのキーが0の場合
            if code[0] == '0':
                if not self.left:
                    self.left = Node(code)
                    cache_left.append(code)
                else:
                    cache_left.append(code)

            # ビットのキーが1の場合
            else:
                if not self.right:
                    self.right = Node(code)
                    tmp_right.append(code)
                else:
                    tmp_right.append(code)

        self.left = Node(cache_left)
        self.right = Node(tmp_right)


class WaveletMatrix:
    def __init__(self):
        self.root = None

    def create_node(self, codes):
        """
        TODO

        キー値のビット列を左から1ビットずつ順番に見ていき, キー値の元になった文字列から
        そのビットに対応する文字を, ビットの値が0の場合(左)とビットの値が1の場合(右)とで分けて取り出し
        それぞれの文字を順番に並べて新たな文字列を作成する.

        取り出した文字列の中の文字が2種類以上の場合は, その文字列に対応する新たなノードを生成し,
        左(または右)の子ノードにする.

        1種類の場合は, 子ノードは生成せず, 処理を終了する.
        """
        if not self.root:
            self.root = Node(codes)
        else:
            self.root.add(codes)


datum_target = "CTCGAGAGTA"
datum_codes = convert(datum_target)

tree = WaveletMatrix()

tree.create_node(datum_codes)

print(tree.root.codes)
tree.create_node(datum_codes)  # ['01', '11', '01', '10', '00', '10', '00', '10', '11', '00']
print(tree.root.left.codes)  # ['01', '01', '00', '00', '00'] == CCAAA
print(tree.root.right.codes)  # ['11', '10', '10', '10', '11'] == TGGGT
