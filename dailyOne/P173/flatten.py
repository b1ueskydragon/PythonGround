def flatten(key_mem, pair):
    """
    Depth-first-search w/t Recursion.

    e.g.
        - 'key' is not a target
        - 'foo' is a target
    """

    for key in pair:
        value = pair.get(key)
        # TODO replace to the other condition
        if type(value) is dict:  # Horizontal find
            print('not end')
            key_mem.append(key)
            flatten(key_mem, value)  # Vertical find
        else:
            print('end')

    return key_mem


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

res = flatten(key_mem=[], pair=given)  # {"A":1, "B.C": 2, "B.D.E": 3}
print(res)
