def flatten(res_pair, key_mem, pair):
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
            flatten(res_pair, key_mem + key + '.', value)  # Vertical find
        else:
            res_pair.update({key_mem + key: value})

    return res_pair


given = \
    {
        "A": 1,
        "B": {
            "C": 2,
            "D": {
                "E": 3 # TODO if value is {} ...
            }
        }
    }

# TODO Try in-place && less params
res = flatten(res_pair={}, key_mem='', pair=given)  # {"A":1, "B.C": 2, "B.D.E": 3}
print(res)
