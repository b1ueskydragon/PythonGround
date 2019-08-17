def move(disks: int):
    paths = []
    x, y, z = "left", "middle", "right"

    def _move(n: int, start: str, to: str, via: str):
        """
        When H(n) is a minimal step that required for moving,
        H(1) = 1,
        H(n) = H(n-1) + H(1) + H(n-1)

        :param n: disks
        :param start: move from
        :param to: move to
        :param via: via to move
        :return: list of string path
        """
        if n < 1:  # H(0) = 0
            return []
        else:
            _move(n - 1, start, via, to)
            paths.append(f"{n}, {start} -> {to}")  # H(1)
            _move(n - 1, via, to, start)

    _move(disks, x, y, z)

    return paths
