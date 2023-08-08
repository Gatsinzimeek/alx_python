def square_matrix_simple(matrix=[]):
    matris = map(lambda row: [n * n for n in row], matrix)
    return list(matris)
