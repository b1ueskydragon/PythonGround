def depth_first_search(u):
    """
    recursive search.

    :param u: at this point
    :return:
    """
    visited[u] = 'gray'
    for gv in graph.get(u):
        if visited[gv] is 'white':
            pre_visit[gv] = u
            depth_first_search(gv)
    visited[u] = 'black'

    return pre_visit


if __name__ == "__main__":
    # to graph (隣接接点が昇順にソーと済み)
    graph = {
        's': {'1', '6', '8'},
        '1': {'s', '2', '3'},
        '2': {'1', '10', '11'},
        '10': {'2'},
        '11': {'2'},
        '3': {'1', '4', '12'},
        '12': {'3'},
        '4': {'3', '5', '13'},
        '13': {'4'},
        '5': {'4', '6', '9'},
        '6': {'s', '5', '7'},
        '7': {'6', '8', '9'},
        '8': {'s', '7', '14'},
        '14': {'8'},
        '9': {'5', '7', 't'},
        't': {'9'}
    }

    # `gray`  分岐の可能性あり
    # `white` 未探索
    # `black` 探索済み
    visited = {}

    # previous visit point of point u (not yet is -1)
    pre_visit = {}

    for v in graph:
        '''initialize'''
        pre_visit[v] = -1
        visited[v] = 'white'

    print(depth_first_search('s'))
