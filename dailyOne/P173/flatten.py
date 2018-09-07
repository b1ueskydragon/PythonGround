def flatten(pair):
    """
    Depth-first-search w/t Recursion.

    e.g.
        - 'key' is not a target
        - 'foo' is a target
    """
    for key in pair.keys():
        value = pair.get(key)
        if type(value) is dict:  # TODO want fix condition
            flatten(value)
        else:
            print(value)

    # return pair


given = \
    {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

flatten(pair=given)
