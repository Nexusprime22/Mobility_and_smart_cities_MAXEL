# Algorithm 2: Return List Ordered by Distances and Alphanumeric Order

def ordered_list(distances, nodes):
    # sort nodes based on distances and then alphanumerically (node value)
    nodes.sort(key=lambda node: (distances[node], node))
    return nodes

nodes = [0, 1, 3, 4, 5, 7]
distances = {0: 0, 1: 5, 3: 2, 4: 6, 5: 10, 7: 3}

ordered_nodes = ordered_list(distances, nodes)
print(ordered_nodes)