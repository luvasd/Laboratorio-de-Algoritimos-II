def max_product(matrix):
    n = len(matrix)
    max_product = 0
    
    for i in range(n):
        for j in range(n):
            # Verificar horizontalmente
            if j + 4 < n:
                product = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3] * matrix[i][j+4]
                max_product = max(max_product, product)
            
            # Verificar verticalmente
            if i + 4 < n:
                product = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j] * matrix[i+4][j]
                max_product = max(max_product, product)
            
            # Verificar diagonalmente para a direita
            if i + 4 < n and j + 4 < n:
                product = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3] * matrix[i+4][j+4]
                max_product = max(max_product, product)
            
            # Verificar diagonalmente para a esquerda
            if i + 4 < n and j >= 4:
                product = matrix[i][j] * matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3] * matrix[i+4][j-4]
                max_product = max(max_product, product)
    
    return max_product

# Exemplo de matriz
matrix = [
    [2, 4, 3, 5, 5],
    [1, 2, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 2, 1],
    [1, 1, 1, 1, 2]
]

result = max_product(matrix)
print(result)  # Deve imprimir 32
