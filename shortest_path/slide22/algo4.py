def floyd_warshall(graph):
    # set the distance matrix with the initial graph
    n = len(graph)
    distances = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            elif j in graph[i]:
                distances[i][j] = graph[i][j]
    
    # Compute all pairs of shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    
    return distances

# graph as an adjacency matrix
graph = {
    0: {0: 0, 1: 5, 2: float('inf'), 3: 2, 4: float('inf'), 5: float('inf'), 6: float('inf'), 7: float('inf'), 8: float('inf')},
    1: {0: 5, 1: 0, 2: float('inf'), 3: float('inf'), 4: 1, 5: float('inf'), 6: float('inf'), 7: 3, 8: float('inf')},
    2: {0: float('inf'), 1: float('inf'), 2: 0, 3: float('inf'), 4: float('inf'), 5: float('inf'), 6: float('inf'), 7: float('inf'), 8: float('inf')},
    3: {0: 2, 1: float('inf'), 2: float('inf'), 3: 0, 4: float('inf'), 5: float('inf'), 6: float('inf'), 7: 8, 8: float('inf')},
    4: {0: float('inf'), 1: 1, 2: float('inf'), 3: float('inf'), 4: 0, 5: float('inf'), 6: float('inf'), 7: float('inf'), 8: float('inf')},
    5: {0: float('inf'), 1: float('inf'), 2: float('inf'), 3: float('inf'), 4: float('inf'), 5: 0, 6: float('inf'), 7: float('inf'), 8: float('inf')},
    6: {0: float('inf'), 1: float('inf'), 2: float('inf'), 3: float('inf'), 4: float('inf'), 5: float('inf'), 6: 0, 7: float('inf'), 8: float('inf')},
    7: {0: float('inf'), 1: 3, 2: float('inf'), 3: 8, 4: float('inf'), 5: float('inf'), 6: float('inf'), 7: 0, 8: float('inf')},
    8: {0: float('inf'), 1: float('inf'), 2: float('inf'), 3: float('inf'), 4: float('inf'), 5: float('inf'), 6: float('inf'), 7: float('inf'), 8: 0}
}

shortest_paths = floyd_warshall(graph)
print(shortest_paths)
