class Node:
    def __init__(self, char='*'):
        self.char = char
        self.children = {}  # {char : Node}
        self.index = 0
        self.word_end = False


def cons(root: Node, word: str):
    curr = root
    for char in word:
        for node in curr.children.values():
            if node.char == char:
                node.index += 1
                curr = node
                break
        else:
            new_node = Node(char)
            curr.children[char] = new_node
            curr = new_node

    curr.word_end = True


def retrieval(word, patt):
    """
    less than O(N * k) worst time.

    :param word: string
    :param patt: pattern
    :return: Start index if pattern found, else False.
    """

    return False


some_trie = Node()
cons(some_trie, "retrieval")
retrieval("retrieval", "trie")  # 2
retrieval("retrieval", "e")  # 1
