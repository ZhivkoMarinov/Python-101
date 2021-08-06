def gas_stations(distance, tank_size, stations):
    result = []
    distance_between = [stations[0]]
    all_spots = [x for x in stations if x < distance] + [distance]
    fuel = tank_size

    for i in range(len(all_spots) - 1):
        distance_between.append(all_spots[i + 1] - all_spots[i])

    for d in distance_between:
        if d >= tank_size:
            return []

    for index, dist in enumerate(distance_between):
        fuel -= dist
        if fuel <= 0:
            result.append(all_spots[index - 1])
            fuel = tank_size - dist

    return result
