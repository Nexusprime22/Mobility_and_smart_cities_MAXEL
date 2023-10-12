print("----")

# Define the set of states
# states = [1, 2, 3, 5, 10, 20, 30]
# print("\nstates:",states)
# # Initialize a set of edges representing the relations between states
# edges = [(1, 5), (1, 10), (1, 20), (2, 10), (2, 20), (3, 10), (3, 20), (5, 10), (5, 20), (10, 20), (20, 30)]
# print("edges before\n"+str(edges))

states = [1, 2, 3, 4, 5]
print("\nstates:",states)
# Initialize a set of edges representing the relations between states
edges = [(1, 3), (3,2), (3,4), (3,5), (4,1)]
print("edges before\n"+str(edges))

def add_transitive_edges(edges):
    for state1 in states:
        for state2 in states:
            if (state1,state2) in edges:
                for state3 in states:
                    if (state2,state3) in edges:
                        if (state1,state3) not in edges:
                            edges.append((state1,state3))
                            print("adding",(state1,state3),"because",(state1,state2),"and",(state2,state3))
                            return edges
    return edges

while True:

    previousLength = len(edges)
    edges = add_transitive_edges(edges)
    if(len(edges)==previousLength):
        break

print("Transitive closure edges:\n" + str(edges))

print("\n----\nMATRIX\n")

# MATRIX

# make transitive closure

def find_transitive_edges_to_add_matrix(matrix):
    n = len(matrix)
    transitive_edges = set()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1:
                        if matrix[i][k] == 0:
                            transitive_edges.add((i,k))
                            # return transitive_edges           
    return transitive_edges

def apply_transitive_closure(matrix):
    n = len(matrix)
    while(True):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    for k in range(n):
                        if matrix[j][k] == 1 and matrix[i][k] == 0:
                            matrix[i][k] = 1
                            # print("set", (i, k), "= 1 because", (i,j), "= 1 and", (j, k),"= 1")
                            # Define a dictionary to map indices to values
                            index_to_value = {0: 1, 1: 2, 2: 3, 3: 5, 4: 10, 5: 20, 6: 30}

                            # Modify the printing
                             # Get the corresponding values using the dictionary
                            i_value = index_to_value[i]
                            j_value = index_to_value[j]
                            k_value = index_to_value[k]
                            print(f"add ({i_value},{k_value}) because ({i_value},{j_value}) and ({j_value},{k_value})")
                            
                            # modification = true
                            return matrix

transitive_closure_matrix = [
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]
print("before")
for row in transitive_closure_matrix:
    print(row)

while True:
    # Find transitive edges in the current set of edges
    transitive_edges = find_transitive_edges_to_add_matrix(transitive_closure_matrix)
    print(transitive_edges)
    # If no more transitive edges are found, break the loop
    if not transitive_edges:
        break
    no_closure = apply_transitive_closure(transitive_closure_matrix)

    print("after")
    for row in no_closure:
        print(row)

print("\n------")
print("SECOND MATRIX")
print("------")

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
print("before")
for row in transitive_closure_matrix:
    print(row)

while True:
    # Find transitive edges in the current set of edges
    transitive_edges = find_transitive_edges_to_add_matrix(transitive_closure_matrix)
    print(transitive_edges)
    # If no more transitive edges are found, break the loop
    if not transitive_edges:
        break
    no_closure = apply_transitive_closure(transitive_closure_matrix)

    print("after")
    for row in no_closure:
        print(row)

#########
# other #
#########

# # Define the set of states
# states = {1, 2, 3, 5, 10, 20, 30}
# print("\nstates:", states)

# # Initialize a set of edges representing the relations between states
# edges = [(1, 5), (1, 10), (1, 20), (2, 10), (2, 20), (3, 10), (3, 20), (5, 10), (5, 20), (10, 20), (20, 30)]
# print("edges before\n" + str(edges))

# # Create an adjacency matrix to represent the graph
# adjacency_matrix = {state: {state} for state in states}

# # Add edges to the adjacency matrix
# for source, target in edges:
#     adjacency_matrix[source].add(target)

# # Warshall's algorithm for transitive closure
# for k in states:
#     for i in states:
#         for j in states:
#             if k != i and k != j:
#                 if j in adjacency_matrix[i] and k in adjacency_matrix[j]:
#                     adjacency_matrix[i].add(k)

# # Extract the transitive closure edges
# transitive_closure_edges = [(source, target) for source in states for target in adjacency_matrix[source] if source != target]

# print("Transitive closure edges:\n" + str(transitive_closure_edges))
