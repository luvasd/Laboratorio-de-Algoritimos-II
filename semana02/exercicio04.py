matrix = [
    [5, 9, 2],
    [4, 7, 1],
    [8, 3, 6]
]

total_sum = 0
row_averages = []

# Calcular a média de cada linha e somar os elementos para a média total
for row in matrix:
    row_sum = 0
    for value in row:
        row_sum += value
    row_average = row_sum / len(row)
    row_averages.append(row_average)
    total_sum += row_sum

# Calcular a média total
total_elements = len(matrix) * len(matrix[0])
matrix_average = total_sum / total_elements

print("Média total da matriz:", matrix_average)
print("Médias das linhas:", row_averages)
