"""
without resizing the underlying array
"""


class struct:
    def __init__(self):
        self._set = []

    def add(self, value):
        """
        Add a value to the set of values.
        """
        pass

    def check(self, value):
        """
        Check whether a value is in the set.
        It may return occasional false positives.
        """
        return True
