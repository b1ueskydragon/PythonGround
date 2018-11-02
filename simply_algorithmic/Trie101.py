"""
edge -> key
node -> incident whether key is exist,
        and whether it is end of a specific word.

if given = ["1011", "10", "011", "100"],
Trie should be

              ●
         /         \
        /           \
      0/             \1
     ("0")           ●
      \1            0/
       ●          ("10")
        \1        0/  \1
     ("011")   ("100") ●
                        \1
                       ("1011")

notes:
      each nodes don't have a key. () is only for explanation.
"""

given = ["1011", "10", "011", "100"]


class Node:
    def __init__(self, char='*'):
        self.char = char
        self.children = []  # TODO {char : Node} mapping
        self.word_finished = False
        self.appeared_counter = 1


def insert(root: Node, word: str):
    node = root
    for char in word:
        found = False
        for child in node.children:
            if child.char == char:
                child.appeared_counter += 1
                node = child
                found = True
                break
        if not found:
            new_child = Node(char)
            node.children.append(new_child)
            node = new_child

    node.word_finished = True  # Mark end


# TODO find prefix

my_trie = Node()
insert(my_trie, "1011")
insert(my_trie, "10")
insert(my_trie, "011")
insert(my_trie, "100")
