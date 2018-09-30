class PrefixMapSum:
    def __init__(self):
        self.map = {}
        # self.enroll = {} # TODO memoing existing search result

    def insert(self, key, value):
        self.map[key] = value

    def sum(self, prefix):
        # should be local variables (Do not setting with params)
        local_res, local_cache = set(), 0

        for key in self.map.keys():
            if key.startswith(prefix):
                local_res.add(key)

        for hit in local_res:
            local_cache += self.map[hit]

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
