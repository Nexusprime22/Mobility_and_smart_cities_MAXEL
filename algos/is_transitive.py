# Representation of data: the 2-dimensional array of the relation
R3 = [[1, 0, 1, 0, 0], 
      [0, 1, 0, 1, 1], 
      [1, 0, 1, 0, 0],
      [0, 1, 0, 1, 1],
      [0, 1, 0, 1, 1]]

# Initialize a variable to check if the relation is transitive
is_transitive = True

# Iterate through the rows (i) and columns (j) of the array
for i in range(len(R3)):
    for j in range(len(R3[i])):
        # Check for a valid relation (x, y)
        if R3[i][j]:
            # Look for (y, z) in the y-line only
            for k in range(len(R3[j])):
                if R3[j][k]:
                    # Verify if R3[x, k] exists
                    # print(R3[i])
                    if not R3[i][k]:
                        print("wrong at coordinates",(i,k))
                        # Transitive property violated
                        is_transitive = False
                        break  # No need to continue checking
        else:
            continue  # No relation for (x, y), move to the next element

# Print the result
if is_transitive:
    print("The relation is transitive.")
else:
    print("The relation is not transitive.")