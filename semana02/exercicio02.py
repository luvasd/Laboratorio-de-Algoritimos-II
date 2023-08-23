l = [1, 1, 2, 2, 3, 4, 5, 6]

l_unicos = []

l_repetidos = []

for i in l:
    if i not in l_unicos and i not in l_repetidos:
        #Se o numero nao estiver el l_unicos e em l_repetidos, ira adicionar em l_unicos
        l_unicos.append(i)
        #print(l_unicos)
        #print(l_repetidos)

    elif i in l_unicos:
        #if ele estiver em l_unicos ira adiconar em l_repetidos e remover de l_unicos
        l_unicos.remove(i)
        l_repetidos.append(i)

print("repetidos:", l_repetidos, "unicos", l_unicos)
