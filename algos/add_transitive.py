def add_transitive_edges(edges, states):
    for state1 in states:
        for state2 in states:
            if (state1,state2) in edges:
                for state3 in states:
                    if (state2,state3) in edges:
                        if (state1,state3) not in edges:
                            edges.append((state1,state3))
                            print("adding",(state1,state3),"because",(state1,state2),"and",(state2,state3))
                            # once an edge is added, no need to further continue, 
                            # we will restart the process with the updated graph
                            return edges
    return edges

def transitive_closure_on_graph(states, edges):

    while True:

        previousLength = len(edges)
        edges = add_transitive_edges(edges, states)
        if(len(edges)==previousLength):
            break

    print("edges after:\n" + str(edges))
    return edges

# set of states
states = [1, 2, 3, 5, 10, 20, 30]
print("\nstates:",states)
# set of edges representing the relations between states
edges = [(1, 5), (1, 10), (1, 20), (2, 10), (2, 20), (3, 10), (3, 20), (5, 10), (5, 20), (10, 20), (20, 30)]
print("edges before:\n"+str(edges))
transitive_closure_on_graph(states,edges)

print("\n----")

# set of states
states = [1, 2, 3, 4, 5]
print("\nstates:",states)
# set of edges representing the relations between states
edges = [(1, 3), (3,2), (3,4), (3,5), (4,1)]
print("edges before:\n"+str(edges))
transitive_closure_on_graph(states,edges)

print("\n----\nMATRIX")
print("------")

# MATRIX

# method to list all transitive links missing
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

def apply_transitive_closure_matrix(matrix, coins=False):
    n = len(matrix)
    while(True):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    for k in range(n):
                        if matrix[j][k] == 1 and matrix[i][k] == 0:
                            matrix[i][k] = 1
                            # in the case without dealing with coins example
                            if(not(coins)):
                                print("set", (i, k), "= 1 because", (i,j), "= 1 and", (j, k),"= 1")
                            # in the case with coins (state id is coin value, for printing)
                            else:
                                # define a dictionary to map indices to values
                                index_to_value = {0: 1, 1: 2, 2: 3, 3: 5, 4: 10, 5: 20, 6: 30}
                                # get the corresponding values using the dictionary
                                i_value = index_to_value[i]
                                j_value = index_to_value[j]
                                k_value = index_to_value[k]
                                print(f"add ({i_value},{k_value}) because ({i_value},{j_value}) and ({j_value},{k_value})")
                                
                            # modification = true
                            return matrix

def operate_on_matrix(matrix, coins=False):
    print("initial_matrix:")
    for row in matrix:
        print(row)

    while True:
        # find transitive edges in the current set of edges
        transitive_edges = find_transitive_edges_to_add_matrix(matrix)
        # print(transitive_edges)
        # if no more transitive edges are found, break the loop
        if not transitive_edges:
            break

        no_closure = apply_transitive_closure_matrix(matrix,coins)

        # print("updated matrix:")
        # for row in no_closure:
        #     print(row)

    print("final matrix:")
    for row in no_closure:
        print(row)

matrix1 = [
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

operate_on_matrix(matrix1)

print("\n------")
print("SECOND MATRIX")
print("------")

matrix2 = [
    # 1 2  3  5 10  20 30
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
]

# to better understand the transitive relations created
# we use a boolean used in method for better comprehension of links created (using coin values)
operate_on_matrix(matrix2, True)