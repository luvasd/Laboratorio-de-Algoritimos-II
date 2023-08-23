matrix = [
    [5, 9, 2],
    [4, 7, 1],
    [8, 3, 6]
]

sum_of_max_values = 0

for row in matrix:
    max_value = row[0]  # Suponha que o primeiro valor da linha seja o máximo
    for value in row:
        if value > max_value:
            max_value = value
    sum_of_max_values += max_value

print("A soma dos maiores valores de cada linha é:", sum_of_max_values)
