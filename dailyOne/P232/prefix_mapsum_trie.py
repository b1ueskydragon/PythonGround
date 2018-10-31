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


'''
Case : 
    Rarely be inserting new words, 
    and need sum retrieval to be very efficient.
'''
mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
print(mapsum.sum("col"))  # 3
mapsum.insert("column", 2)
mapsum.insert("cool", 4)
print(mapsum.sum("co"))  # 9
print(mapsum.sum("col"))  # 5
print(mapsum.sum("A"))  # 0

'''
Trouble :
    if new word comes, 'dict' object has no attribute 'total'
'''
# mapsum.insert("Alex", 1)
# print(mapsum.sum("A"))  # 1
# print(mapsum.sum("col"))  # 5
# mapsum.insert("columnar", 4)
# print(mapsum.sum("col"))  # 6

print(mapsum.map)
