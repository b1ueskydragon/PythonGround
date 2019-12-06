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
        return _subsequence(s=s[1:], ps=ps + [l + [h] for l in ps])

    return list(map(''.join, _subsequence(string, [[]])))
