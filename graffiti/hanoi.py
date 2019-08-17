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
        elif n == 1:
            paths.append(f"{start} -> {to}")
        else:
            _move(n - 1, start, via, to)
            _move(1, start, to, via)
            _move(n - 1, via, to, start)

    _move(disks, x, y, z)

    return paths
