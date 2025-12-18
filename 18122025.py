def create_board(dimensions):
    result = [[None] * dimensions[1] for _ in range(dimensions[0])]
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if (i+j) % 2 == 0:
                result[i][j] = "X"
            else:
                result[i][j] = "O"
    return result