from codeit_kr.bfs import station as new

"""
파일의 데이터를 정리하여 각 역에 해당하는 Station 인스턴스를 만들고,
add_connection 메소드로 이웃 역들을 연결시킨다.
후에 각 역을 쉽게 찾아서 쓸 수 있도록 stations 사전의
key 로 역 이름을 넣고, value 로 해당 Station 인스턴스를 넣는다.
"""
stations = {}
in_file = open('stations.txt')

for ln in in_file:
    line = [_ for _ in ln.split() if _ != '-']
    l, r = -1, 1
    for st in line:
        ins = new.Station(st)
        if l > -1 and line[l]:
            ins.add_connection(new.Station(line[l]))
        if r < len(line) and line[r]:
            ins.add_connection(new.Station(line[r]))
        l += 1
        r += 1
        stations[st] = ins

in_file.close()

# # Test
# start_name = "이태원"
# goal_name = "잠원"
#
# start = stations[start_name]
# goal = stations[goal_name]
#
# path = bfs(start, goal)
# for station in path:
#     print(station.name)
