def find_transitive_edges(edges):
    transitive_edges = []
    
    for edge1 in edges:
        for edge2 in edges:
            if edge1[0]!=edge1[1] and edge2[0]!=edge2[1] and edge1[1] == edge2[0] and edge1 != edge2:
                transitive_edge = (edge1[0], edge2[1])
                # print(transitive_edge)
                if transitive_edge not in transitive_edges and transitive_edge in edges:
                    print("Transitive relation to remove found:", transitive_edge, "because", edge1, "and", edge2)
                    transitive_edges.append(transitive_edge)

    return transitive_edges

def subtract_transitive_edges(edges, transitive_edges):
    # Remove elements from the main list
    res = [x for x in edges if x not in transitive_edges]
    return res

def tr_graph(edges):
    print("original edges:",edges,"")
    while True:
        # Find transitive edges in the current set of edges
        transitive_edges = find_transitive_edges(edges)
        # print("transitive_edges found:", transitive_edges)
        # If no more transitive edges are found, break the loop
        if not transitive_edges:
            break
        # Subtract transitive edges from the set of edges
        edges = subtract_transitive_edges(edges, transitive_edges)
        print("new set of edges:",edges)
    # Print the final set of edges with removed transitive relations
    print("\n"+str(edges))
    print("\n----------\n")

print("")
# Define the set of states
states = [1, 2, 3, 4]
print("states:",states)
# Initialize a set of edges representing the relations between states
edges = [(1, 1), (1, 2), (2, 3), (3,4), (4,1), (4,2)]
tr_graph(edges)

print("second graph example")
# Define the set of states
states = [1, 2, 3, 5, 10, 20, 30]
print("states:",states)
# Initialize a set of edges representing the relations between states
edges = [(1, 5), (1, 10), (1, 20), (2, 10), (2, 20), (3, 10), (3, 20), (5, 10), (5, 20), (10, 20), (20, 30)]
tr_graph(edges)

print("third graph example")
# Define the set of states
states = [1, 2, 3, 4, 5]
print("states:",states)
# Initialize a set of edges representing the relations between states
edges = [(1, 3), (3, 2), (3, 5), (4,1)]
tr_graph(edges)

##################
# MATRIX
##################

# transitive_closure_matrix = [
#     [1, 1, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1],
#     [1, 1, 0, 0]
# ]

transitive_closure_matrix = [
    # 1 2  3  5 10  20 30
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
]

print("initial matrix:")
for row in transitive_closure_matrix:
    print(row)
def find_transitive_edges_matrix(matrix):
    n = len(matrix)
    transitive_edges = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1 and matrix[i][k] == 1:
                        transitive_edges.append((i,k))
                        return transitive_edges

    return transitive_edges

def remove_transitive_closure(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1 and matrix[i][k] == 1:
                        print("0 at index",(i,k),"because 1 at",(i,j),"and 1 at",(j,k))
                        matrix[i][k] = 0
                        return matrix
    return matrix

while True:
    # Find transitive edges in the current set of edges
    transitive_edges = find_transitive_edges_matrix(transitive_closure_matrix)

    # If no more transitive edges are found, break the loop
    if not transitive_edges:
        break
    no_closure = remove_transitive_closure(transitive_closure_matrix)

    print("after")
    for row in no_closure:
        print(row)

