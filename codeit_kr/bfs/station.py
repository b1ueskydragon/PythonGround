class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_connection(self, another_station):
        self.neighbors.append(another_station)  # debug another_station.name
        another_station.neighbors.append(self)  # debug self.name
