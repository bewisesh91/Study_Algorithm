# BFS를 이용한 최단 경로 알고리즘
from collections import deque

class StationNode :
    def __init__(self, station_name) :
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = False

    def add_connection(self, station) :
        self.adjacent_stations.append(station)
        station.adjacent_stations.append(self)


def bfs(graph, start_node) :
    queue = deque()

    for station_node in graph.value() :
        station_node.visited = False
        station_node.predecessor = None

    start_node.visited = True
    queue.append(start_node)

    while queue :
        current_station = queue.popleft()
        for neighbor in current_station.adjacent_stations :
            if not neighbor.visited :
                neighbor.visited = True
                neighbor.predecessor = current_station
                queue.append(neighbor)

def back_track(destination_node) :
    res_str = ""
    temp = destination_node
    while temp is not None :
        res_str = f'{temp.station_name} {res_str}'
        temp = temp.predecessor
    
    return res_str