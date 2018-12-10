"""
without resizing the underlying array
"""


class Struct:
    def __init__(self, size):
        self.size = size
        self.struct = [None] * size

    def add(self, value):
        """
        Add a value to the set of values.
        """
        self.struct[hash(value) % self.size] = value

    def check(self, value):
        """
        Check whether a value is in the set.
        It may return occasional false positives.
        """
        return self.struct[hash(value) % self.size] is not None


# tests
my_struct = Struct(31)
my_struct.add('alex')
my_struct.add('ke')
my_struct.add('metteji')
my_struct.add('metteji')

print(my_struct.struct)

print(my_struct.check('alex'))
print(my_struct.check('alegon'))
print(my_struct.check('metteji'))
print(my_struct.check('mettegi'))
