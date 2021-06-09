# BFS(Breadth First Search)
from collections import deque

class StationNode :
    def __init__(self, station_name) :
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = None

    def add_connection(self, station) :
        self.adjacent_stations.append(station)
        station.adjacent_stations.append(self)


def bfs(graph, start_node) :
    queue = deque()

    for station_node in graph.values() :
        station_node.visited = False

    start_node.visited = True
    queue.append(start_node)

    while queue :
        current_station = queue.popleft()
        for neighbor in current_station.adjacent_stations :
            if not neighbor.visitied :
                neighbor.visited = True
                queue.append(neighbor)

    


    

