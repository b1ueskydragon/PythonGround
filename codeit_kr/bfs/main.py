from codeit_kr.bfs import station as new
from codeit_kr.bfs import bfs as f

"""
파일의 데이터를 정리하여 각 역에 해당하는 Station 인스턴스를 만들고,
add_connection 메소드로 이웃 역들을 연결시킨다.
후에 각 역을 쉽게 찾아서 쓸 수 있도록 stations 사전의
key 로 역 이름을 넣고, value 로 해당 Station 인스턴스를 넣는다.
"""
stations = {}
in_file = open('stations.txt')

for ln in in_file:
    prev = None
    lines = ln.strip().split('-')
    for station in lines:
        name = station.strip()
        if name not in stations.keys():  # 名前が辞書に無い時のみ new instance
            st = new.Station(name)
            stations[name] = st
        else:
            st = stations[name]

        if prev:
            st.add_connection(prev)
        prev = st

in_file.close()

# Test
# for k, v in stations.items():
#     print(k, [st.name for st in v.neighbors])

# Test
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = f.bfs(start, goal)
for station in path:
    print(station.name)
