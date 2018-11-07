"""
Using prefix tree (trie) edition
  - k is the length of the prefix.
"""
from collections import defaultdict


class Trie:
    def __init__(self):
        self.chars = defaultdict(dict)
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

    def sum(self, prefix: str) -> int:
        """
        O(k)
        """
        curr = self.root
        for char in prefix:
            curr = curr.chars[char]
        return curr.total if curr else 0


# words example from https://en.wikipedia.org/wiki/Trie
# retrieval speed is depends on `length of a target key` regardless of the total size of trie.
mapsum = PrefixMapSum()
mapsum.insert("A", 15)
mapsum.insert("to", 7)
mapsum.insert("tea", 3)
mapsum.insert("ted", 4)
mapsum.insert("ten", 12)
mapsum.insert("i", 11)
mapsum.insert("in", 5)
