def isTransitive(matrix):

    print("Matrix:")
    for row in matrix:
        print(row)

    # Iterate through the rows (i) and columns (j) of the array
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check for a valid relation (x, y)
            if matrix[i][j]==1:
                # Look for (y, z) in the y-line only
                for k in range(len(matrix[j])):
                    if matrix[j][k]:
                        # Verify if matrix[x, k] exists
                        # print(matrix[i])
                        if not matrix[i][k]:
                            print("0 at coordinates",(i,k),"while there are 1 at",(i,j), "and", (j,k))
                            print("The matrix is not transitive")
                            return False
            else:
                continue  # no relation for (x, y), move to the next element

    print("The matrix is transitive")
    return True

# 2d array showing the relations
R3 = [[1, 0, 1, 0, 0], 
      [0, 1, 0, 1, 1], 
      [1, 0, 1, 0, 0],
      [0, 1, 0, 1, 1],
      [0, 1, 0, 1, 1]]

isTransitive(R3)

print("----")

# 2d array showing the relations
matrix = [
      [1, 0, 1, 0, 0], 
      [0, 1, 0, 1, 1], 
      [1, 0, 1, 0, 0],
      [0, 1, 0, 1, 1],
      [0, 1, 1, 1, 1]
    ]

isTransitive(matrix)