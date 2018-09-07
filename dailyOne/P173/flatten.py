def flatten(nested):
    return nested


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

print(flatten(nested=given))
