def flatten(pair):
    """
    Depth-first-search w/t Recursion.

    e.g.
        - 'key' is not a target
        - 'foo' is a target
    """

    flatted = {}  # TODO in-place

    for key in pair:
        value = pair.get(key)
        try:  # TODO without exception handling
            flatten(value)
        except:
            print(key, value)


given = \
    {
        "A": 1,
        "B": {
            "C": 2,
            "D": {
                "E": 3
            }
        }
    }

flatten(pair=given)  # {"A":1, "B.C": 2, "B.D.E": 3}
