import collections
import math

# An intersection can be represented as a namedtuple
Intersection = collections.namedtuple('Intersection', ['route', 'distance_from_start', 'distance_to_goal', 'total_distance'])

def shortest_path(M,start,goal):
    explored = []
    frontiers = {}

    for neighbour in M.roads[start]:
        route = [start, neighbour]
        distance_from_start = math.sqrt((M.intersections[start][0] - M.intersections[neighbour][0])**2 + (M.intersections[start][1] - M.intersections[neighbour][1])**2)
        distance_to_goal = math.sqrt((M.intersections[goal][0] - M.intersections[neighbour][0])**2 + (M.intersections[goal][1] - M.intersections[neighbour][1])**2)
        total_distance = distance_from_start + distance_to_goal
        frontiers[neighbour] = Intersection(route, distance_from_start, distance_to_goal, total_distance)

    explored.append(start)

    while frontiers:
        smallest_frontier = sorted(frontiers.items(), key=lambda x: x[1].total_distance)[0]
        smallest_fron_key = smallest_frontier[0]
        explored.append(smallest_fron_key)
        if smallest_fron_key == goal:
            print("shortest path called")
            return smallest_frontier[1].route

        for neighbour in M.roads[smallest_fron_key]:
            if neighbour not in explored:
                route = smallest_frontier[1].route.append(neighbour)
                distance_from_start = smallest_frontier[1].distance_from_start + math.sqrt(
                    (M.intersections[smallest_fron_key][0] - M.intersections[neighbour][0])**2 + (M.intersections[smallest_fron_key][1] - M.intersections[neighbour][1])**2
                    )
                distance_to_goal = math.sqrt((M.intersections[goal][0] - M.intersections[neighbour][0])**2 + (M.intersections[goal][1] - M.intersections[neighbour][1])**2)
                total_distance = distance_from_start + distance_to_goal
                if frontiers.get(neighbour) != None and total_distance > frontiers[neighbour].total_distance:
                    continue
                frontiers[neighbour] = Intersection(route, distance_from_start, distance_to_goal, total_distance)

    if not frontiers:
        return -1