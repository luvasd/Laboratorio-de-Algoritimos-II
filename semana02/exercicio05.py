matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Somar as matrizes elemento por elemento
for i in range(3):
    for j in range(3):
        result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

# Imprimir a matriz resultante
for row in result_matrix:
    print(row)
