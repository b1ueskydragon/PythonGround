"""
Using prefix tree (trie) edition
  - k is the length of the prefix.
"""


class Trie:
    def __init__(self):
        self.chars = {}
        self.total = 0


class PrefixMapSum:
    def __init__(self):
        self.map = {}
        self.root = Trie()

    def insert(self, key: str, value: int):
        """
        associate each letter with a dictionary
        O(k)
        """
        value -= self.map.get(key, 0)  # if key does not exist, return value 0
        self.map[key] = value

        curr = self.root
        for char in key:
            curr = curr.chars.setdefault(char, Trie())  # if char does not exist, return Trie() to default
            curr.total += value

    def sum(self, prefix: str):
        """
        O(k)
        """
        return


mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
mapsum.insert("column", 2)
mapsum.insert("col", 9)
mapsum.insert("cool", 4)
mapsum.insert("Alex", 1)
mapsum.insert("columnar", 4)

print(mapsum.map)
