matriz = [
    [2, 5, 7],
    [5, 1, 8],
    [7, 8, 9]
]

respost = True
parar = False

for lin in range(len(matriz)):
    if parar == True:
        break

    for elemt in range(len(matriz[lin])):
        if matriz[lin][elemt] != matriz[elemt][lin] or len(matriz) != len(matriz[lin]):
            respost = False
            parar = True
            break
        else:
            respost = True

print(respost)
