def flatten(pair):
    for key in pair.keys():
        is_end(pair.get(key))

    # return nested


def is_end(value):
    """
    Depth-first-search w/t Recursion.

    e.g.
        - 'key' is not a target
        - 'foo' is a target
    """
    if type(value) is dict:  # TODO want fix
        for key in value.keys():
            print(value.get(key))
    else:
        print(value)

    return True


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

print(flatten(pair=given))
