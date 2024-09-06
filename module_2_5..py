def get_matrix(n, m, value):
    matrix = []
    list_ = []
    for i in range(m):
        list_.append(value)
    for j in range(n):
        matrix.append(list_[:])
    print(matrix)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)