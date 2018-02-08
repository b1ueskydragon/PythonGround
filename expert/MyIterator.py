"""
Expert Python Programming page 65
Sample code
"""


class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        """Returns the next element."""
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    __next__ = next  # Python3系用

    def __iter__(self):
        """Returns the iterator itself."""
        return self


for el in MyIterator(4):
    print(el)
