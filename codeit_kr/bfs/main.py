stations = {}
in_file = open('stations.txt')

# file to instance Station
# add_connection
# stations = {station_name : Station}

in_file.close()

# Test
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)
