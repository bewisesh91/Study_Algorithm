# DFS(Depth First Search)
from collections import deque

class StationNode :
    def __init__(self, station_name) :
        self.station_name = station_name
        self.visited = 0
        self.adjacent_stations = []

    def add_connection(self, other_station) :
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)


def dfs(graph, start_node) :
    stack = deque()

    for station_node in graph.values() :
        station_node.visited = 0

    start_node.visitied = 1
    stack.append(start_node)

    while stack :
        current_station = stack.pop()
        current_station.visited = 2
        for neighbor in current_station.adjacent_stations:
            if not neighbor.visited == 2 :
                neighbor.visited = 1
                stack.append(neighbor)