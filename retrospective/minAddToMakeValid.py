def min_add_to_make_valid(braces: str):
    add_close = 0
    add_open = 0
    _open, _close = "{", "}"

    for c in braces:
        if c == _open:
            add_close += 1
        elif c == _close and add_close != 0:
            add_close -= 1
        else:  # c == _close but add_close == 0
            add_open += 1

    return add_close + add_open
