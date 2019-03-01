class Station:
    def __init__(self, name):
        name = ""
        self.neighbors = []

    def add_connection(self, another_station):
        self.neighbors.append(another_station)
        another_station.neighbors.append(self)
