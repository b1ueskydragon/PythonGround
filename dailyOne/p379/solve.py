def subsequence(string: str):
    """
    [[]]                              = [[]]

    [[]] + [[] + [x]]                 = [[], [x]]

    [[], [x]] + [[] + [y], [x] + [y]] = [[], [x], [y], [xy]]

    [[], [x], [y], [xy]] + [[] + [z], [x] + [z], [y] + [z], [xy] + [z]]
                                      = [[], [x], [y], [xy], [z], [xz], [yz], [xyz]
    """
    def _subsequence(s: str, ps: [[str]]) -> [[str]]:
        if not s:
            return ps
        h = s[0]
        new_ps = []
        for l in ps:
            new_ps.append(l + [h])
        return _subsequence(s[1:], ps + new_ps)

    return list(map(''.join, _subsequence(string, [[]])))
