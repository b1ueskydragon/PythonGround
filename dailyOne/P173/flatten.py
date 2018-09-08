def flatten(pair):
    """
    Depth-first-search w/t Recursion.

    e.g.
        - 'key' is not a target
        - 'foo' is a target
    """
    for key in pair:
        value = pair.get(key)
        if type(value) is dict:  # TODO want fix condition
            print(key)
            flatten(value)
        else:
            print(key, value)

    # return pair


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
