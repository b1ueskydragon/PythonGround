class Node:
    def __init__(self, val, prev: 'Node', next: 'Node', child: 'Node'):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # in-place
        return head


if __name__ == '__main__':
    head = {"$id": "1",
            "child": None,
            "next": {"$id": "2",
                     "child": None,
                     "next": {"$id": "3",
                              "child": {"$id": "7",
                                        "child": None,
                                        "next": {"$id": "8",
                                                 "child": {
                                                     "$id": "11",
                                                     "child": None,
                                                     "next": {
                                                         "$id": "12",
                                                         "child": None,
                                                         "next": None,
                                                         "prev": {"$ref": "11"},
                                                         "val": 12},
                                                     "prev": None,
                                                     "val": 11},
                                                 "next": {
                                                     "$id": "9",
                                                     "child": None,
                                                     "next": {
                                                         "$id": "10",
                                                         "child": None,
                                                         "next": None,
                                                         "prev": {"$ref": "9"},
                                                         "val": 10},
                                                     "prev": {"$ref": "8"},
                                                     "val": 9},
                                                 "prev": {"$ref": "7"},
                                                 "val": 8},
                                        "prev": None,
                                        "val": 7},
                              "next": {"$id": "4",
                                       "child": None,
                                       "next": {"$id": "5",
                                                "child": None,
                                                "next": {
                                                    "$id": "6",
                                                    "child": None,
                                                    "next": None,
                                                    "prev": {"$ref": "5"},
                                                    "val": 6},
                                                "prev": {"$ref": "4"},
                                                "val": 5},
                                       "prev": {"$ref": "3"},
                                       "val": 4},
                              "prev": {"$ref": "2"},
                              "val": 3},
                     "prev": {"$ref": "1"},
                     "val": 2},
            "prev": None,
            "val": 1}

    expected = {"$id": "1",
                "child": None,
                "next": {"$id": "2",
                         "child": None,
                         "next": {"$id": "3",
                                  "child": None,
                                  "next": {"$id": "4",
                                           "child": None,
                                           "next": {"$id": "5",
                                                    "child": None,
                                                    "next": {
                                                        "$id": "6",
                                                        "child": None,
                                                        "next": {
                                                            "$id": "7",
                                                            "child": None,
                                                            "next": {
                                                                "$id": "8",
                                                                "child": None,
                                                                "next": {
                                                                    "$id": "9",
                                                                    "child": None,
                                                                    "next": {
                                                                        "$id": "10",
                                                                        "child": None,
                                                                        "next": {
                                                                            "$id": "11",
                                                                            "child": None,
                                                                            "next": {
                                                                                "$id": "12",
                                                                                "child": None,
                                                                                "next": None,
                                                                                "prev": {"$ref": "11"},
                                                                                "val": 6},
                                                                            "prev": {"$ref": "10"},
                                                                            "val": 5},
                                                                        "prev": {"$ref": "9"},
                                                                        "val": 4},
                                                                    "prev": {"$ref": "8"},
                                                                    "val": 10},
                                                                "prev": {"$ref": "7"},
                                                                "val": 9},
                                                            "prev": {"$ref": "6"},
                                                            "val": 12},
                                                        "prev": {"$ref": "5"},
                                                        "val": 11},
                                                    "prev": {"$ref": "4"},
                                                    "val": 8},
                                           "prev": {"$ref": "3"},
                                           "val": 7},
                                  "prev": {"$ref": "2"},
                                  "val": 3},
                         "prev": {"$ref": "1"},
                         "val": 2},
                "prev": None,
                "val": 1}
