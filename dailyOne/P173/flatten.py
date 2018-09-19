def flatten(pair, res_pair={}, key_mem=''):
    """
    Depth-first-search w/t Recursion.

    e.g.
        - 'key' is not a target
        - 'foo' is a target
    """

    for key in pair:
        value = pair.get(key)
        # TODO other possible condition
        if isinstance(value, dict):  # Horizontal find
            flatten(value, res_pair, key_mem + key + '.')  # Vertical find
        else:
            res_pair.update({key_mem + key: value})

    return res_pair


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

# TODO Try in-place
res = flatten(pair=given)  # {"A":1, "B.C": 2, "B.D.E": 3}
print(res)
