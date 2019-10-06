class PrefixMapSum:
    def __init__(self):
        self.map = {}

    def insert(self, key, value):
        """
        O(1)
        """
        self.map[key] = value

    # def sum(self, prefix):
    #     local_hit = set()
    #
    #     for key in self.map.keys():
    #         if key.startswith(prefix):
    #             local_hit.add(key)
    #
    #     return sum([self.map[_] for _ in local_hit])

    def _sum(self, prefix):
        """
        O(N*k)
          - k is the length of the prefix.
        """
        return sum([val for key, val in self.map.items() if key.startswith(prefix)])


mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
print(mapsum._sum("col"))  # 3
mapsum.insert("column", 2)
mapsum.insert("cool", 4)
print(mapsum._sum("co"))  # 9
print(mapsum._sum("col"))  # 5
print(mapsum._sum("A"))  # 0
mapsum.insert("Alex", 1)
print(mapsum._sum("A"))  # 1
print(mapsum._sum("col"))  # 5
mapsum.insert("columnar", 4)
print(mapsum._sum("col"))  # 6

print(mapsum.map)
