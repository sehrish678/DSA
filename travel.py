import heapq

def dijkstra(graph, start, end):
    """
    Find the shortest path between two locations using Dijkstra's algorithm.
    :param graph: Dictionary representing the graph (adjacency list).
    :param start: Starting location.
    :param end: Destination location.
    :return: Tuple (shortest distance, path as a list of locations).
    """
    priority_queue = [(0, start, [])]  # (current_distance, current_node, path_so_far)
    visited = set()

    while priority_queue:
        (current_distance, current_node, path) = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        path = path + [current_node]

        # If we reached the destination, return the distance and path
        if current_node == end:
            return current_distance, path

        # Explore neighbors
        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (current_distance + weight, neighbor, path))

    return float("inf"), []  # If no path exists

graph = {
    "Karachi": {"Lahore": 4, "Islamabad": 2},
    "Lahore": {"Karachi": 4, "Islamabad": 1, "Peshawar": 5},
    "Islamabad": {"Karachi": 2, "Lahore": 1, "Peshawar": 8, "Quetta": 10},
    "Peshawar": {"Lahore": 5, "Islamabad": 8, "Quetta": 2},
    "Quetta": {"Islamabad": 10, "Peshawar": 2}
}


# User input
start_location = input("Enter the starting location: ")
end_location = input("Enter the destination: ")

if start_location not in graph or end_location not in graph:
    print("One or both locations are not in the graph.")
else:
    distance, path = dijkstra(graph, start_location, end_location)

    if distance == float("inf"):
        print(f"No path found from {start_location} to {end_location}.")
    else:
        print(f"Shortest distance from {start_location} to {end_location}: {distance}")
        print(f"Path: {' ->'.join(path)}")
