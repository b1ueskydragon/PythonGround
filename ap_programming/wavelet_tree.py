import math

"""
AP 2018 A 3

キー値のビット列を左から1ビットずつ順番に見ていき, キー値の元になった文字列から
そのビットに対応する文字を, ビットの値が0の場合(左)とビットの値が1の場合(右)とで分けて取り出し
それぞれの文字を順番に並べて新たな文字列を作成する.

取り出した文字列の中の文字が2種類以上の場合は, その文字列に対応する新たなノードを生成し,
左(または右)の子ノードにする.

1種類の場合は, 子ノードは生成せず, 処理を終了する.
"""

"""
A pair of (string : code)

If the pair is (C : 01),
code of string C is 01,

0 is a `key`
1 is a `value` of a key 
"""
code_map: dict = {'A': '000', 'C': '001', 'G': '010', 'T': '011', 'X': '100', 'Y': '101', 'Z': '110', 'W': '111'}


def convert(string):
    """ Convert string to code. """
    res = []
    for c in string:
        if c in code_map:
            res.append(code_map[c])
    return res


def revert(codes: list, pairs: dict = code_map):
    """
    revert(['01', '01', '00', '00', '00']) == 'CCAAA'
    """
    revert_map = {v: k for k, v in pairs.items()}
    return ''.join([revert_map[code] for code in codes if code in revert_map])


# def extract_key(code):
#     return ''.join([code[i] for i in range(len(code)) if i % 2 == 0])


"""
image>
         CTCGAGAGTA
        /          \
    CCAAA         TGGGT
    /   \         /   \
  AAA   CC      GGG   TT

"""


class Node:
    def __init__(self, codes, i):
        # for create a each node
        self.codes = codes
        self.cache_left = []
        self.cache_right = []

        self.left = None
        self.right = None

        self._concat(codes, i)

    def _concat(self, codes, i):
        """
        ノードの深さに応じて決まるビット一のビットの値を取り出し,
        文字の並びと同じ順番で並べてビット列として構成したものを
        キー値としてノードに登録する.

        :param codes: ビット列
        :param i: キーとなる文字の index
        """
        for code in codes:
            # ビットのキーが0の場合
            if code[i] == '0':
                self.cache_left.append(code)
            # ビットのキーが1の場合
            else:
                self.cache_right.append(code)

    def add(self, i):
        if self.cache_left:
            if self.left:
                self.left.add(i)
            else:
                self.left = Node(self.cache_left, i)

        if self.cache_right:
            if self.right:
                self.right.add(i)
            else:
                self.right = Node(self.cache_right, i)


class WaveletMatrix:
    def __init__(self, depth):
        self.root = None
        self.depth = depth

    def _create_node(self, codes):
        for i in range(self.depth):
            if not self.root:
                self.root = Node(codes, i)
            else:
                self.root.add(i)

    def create_nodes(self, codes):
        for i in range(self.depth):
            self._create_node(codes)


def printr(codes):
    print(revert(codes))


"""
e.g.)

root ['01', '11', '01', '10', '00', '10', '00', '10', '11', '00']

left ['01', '01', '00', '00', '00'] == CCAAA
right ['11', '10', '10', '10', '11'] == TGGGT
"""

datum_target = "CTWCGAGAGTAXYZ"
datum_codes = convert(datum_target)
DEPTH = int(math.log2(len(code_map)))  # TODO len(code_map) or len(set(datum_target))

tree = WaveletMatrix(DEPTH)  # ビット列の長さ == log2文字の種類

tree.create_nodes(datum_codes)

printr(tree.root.codes)  # 根は深さ0

printr(tree.root.left.codes)
printr(tree.root.right.codes)

printr(tree.root.left.left.codes)
printr(tree.root.left.right.codes)

printr(tree.root.left.left.left.codes)
printr(tree.root.left.left.right.codes)

printr(tree.root.left.right.left.codes)
printr(tree.root.left.right.right.codes)

printr(tree.root.right.left.codes)
printr(tree.root.right.right.codes)

printr(tree.root.right.left.left.codes)
printr(tree.root.right.left.right.codes)

printr(tree.root.right.right.left.codes)
printr(tree.root.right.right.right.codes)
