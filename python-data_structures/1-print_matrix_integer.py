def print_matrix_integer(matrix=[[]]):
    sign = "$"
    for i in matrix:
        for index,j in enumerate(i):
            print('{}'.format(j), end='')
            if index < len(i) - 1:
                print(" ", end='')
        print(sign)
