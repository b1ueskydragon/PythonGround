given = ["1011", "10", "011", "100"]


class Node:
    def __init__(self, char='*'):
        self.char = char
        self.children = {}  # {char : Node}
        self.word_finished = False
        self.appeared_counter = 1


def insert(root: Node, word: str):
    node = root
    for char in word:
        for child in node.children.values():
            if child.char == char:
                child.appeared_counter += 1
                node = child
                break
        else:  # child was not found in the present node(child).
            new_child = Node(char)
            node.children[char] = new_child
            node = new_child

    node.word_finished = True  # Mark end


def find_prefix(root: Node, prefix: str):
    node = root

    if not root.children:
        return 0

    for char in prefix:
        for child in node.children.values():
            if child.char == char:
                node = child
                break
        else:  # return anyway if char was not found
            return 0

    return node.appeared_counter


my_trie = Node()
insert(my_trie, "1011")
insert(my_trie, "10")
insert(my_trie, "011")
insert(my_trie, "100")

print(find_prefix(my_trie, '0'))
print(find_prefix(my_trie, '1011'))
print(find_prefix(my_trie, '1'))
print(find_prefix(my_trie, '1001'))
print(find_prefix(my_trie, '100'))
print(find_prefix(my_trie, '1'))
print(find_prefix(my_trie, '11'))
print(find_prefix(my_trie, '011'))
