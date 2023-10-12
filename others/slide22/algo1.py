# Algorithm 1: Calculate Shortest Paths from Any Point to 0

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    unvisited_nodes = list(graph.keys())

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])

        unvisited_nodes.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

graph = {
    0: {1: 5, 3: 2},
    1: {0: 5, 4: 1, 7: 3},
    3: {0: 2, 7: 8},
    4: {1: 1},
    5: {},
    7: {},
}

shortest_distances = dijkstra(graph, 0)
print(shortest_distances)
