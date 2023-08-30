def sum_below_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_sum = 0
    
    for i in range(rows):
        for j in range(cols):
            if i > j:
                total_sum += matrix[i][j]
                
    return total_sum

# Exemplo de matriz 3x3, substitua pelos seus próprios valores
matrix = [
    [0, 2, 3],
    [4, 10, 6],
    [7, 8, 20]
]

result = sum_below_diagonal(matrix)
print(f"A soma dos elementos abaixo da diagonal principal é: {result}")
