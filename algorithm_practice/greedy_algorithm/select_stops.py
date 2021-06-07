def select_stops(water_stops, capacity) :
    start = 0
    stops = []
    for i in range(len(water_stops)) :
        if water_stops[i] - start > capacity :
            stops.append(water_stops[i-1])
            start = water_stops[i-1]

    stops.append(water_stops[-1])

    return stops

list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))