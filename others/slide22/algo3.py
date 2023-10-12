# Algorithm 3 which calculates the sublist L0 corresponding to the subgraph G0 = (N0, EO) = G \ {2,4,6,8} 

def calculate_sublist_L0(L, excluded_nodes):
    # Filter out the excluded nodes from L
    L0 = [node for node in L if node not in excluded_nodes]
    return L0

L = [0, 5, 7, 1, 3, 4]
excluded_nodes = [2, 4, 6, 8]

L0 = calculate_sublist_L0(L, excluded_nodes)
print(L0)
