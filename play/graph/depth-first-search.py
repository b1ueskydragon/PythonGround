# to graph
graph = {
    's': {'1', '6', '8'},
    '1': {'s', '2'},
    '2': {'1', '10', '11'},
    '3': {'1', '3', '12'},
    '4': {'3', '5', '13'},
    '5': {'4', '6', '9'},
    '6': {'s', '5', '7'},
    '7': {'6', '8', '9'},
    '8': {'s', '7', '14'},
    '9': {'5', '7', 't'},
    '10': {'2'},
    '11': {'2'},
    '12': {'3'},
    't': {'9'}
}

# visited (not yet is -1)
visited = {}

# previous visit point of point u
previous_visit = {}


def depth_first_search(u):
    '''
    recursive search

    :param u: at this point
    :return:
    '''
    visited[u] = 'gray'
    for v in graph:
        if visited[v] is 'white':
            previous_visit[v] = u
            depth_first_search(v)
    visited[u] = 'black'


if __name__ == "__main__":
    for v in graph:
        '''
        initialize
        '''
        previous_visit[v] = -1
        visited[v] = 'white'

    print(depth_first_search('s'))
