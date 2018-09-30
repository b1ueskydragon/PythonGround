class PrefixMapSum:
    def __init__(self):
        self.map = {}
        self.enroll = {}  # memoing existing search result globally.

    def insert(self, key, value):
        self.map[key] = value

    def sum(self, prefix):
        if prefix in self.enroll:
            local_hit = self.enroll[prefix]
        else:
            local_hit = set()

        local_cache = 0

        for key in self.map.keys():
            if key.startswith(prefix):
                local_hit.add(key)

        for hit in local_hit:
            local_cache += self.map[hit]

        self.enroll[prefix] = local_hit

        return local_cache


mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
print(mapsum.sum("col"))  # 3
mapsum.insert("column", 2)
mapsum.insert("cool", 4)
print(mapsum.sum("co"))  # 9
print(mapsum.sum("col"))  # 5
print(mapsum.sum("A"))  # 0
mapsum.insert("Alex", 1)
print(mapsum.sum("A"))  # 1
print(mapsum.sum("col"))  # 5
mapsum.insert("columnar", 4)
print(mapsum.sum("col"))  # 6

print(mapsum.map, mapsum.enroll)
