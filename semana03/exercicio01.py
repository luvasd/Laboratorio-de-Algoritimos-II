import random


def validate_number(matriz, number):
    for line in range(len(matriz)):
        for column in range(len(matriz[line])):
            if matriz[line][column] == number:
                return False
            
    return True


def generate_bingo():
    matriz = []

    for line in range(5):
        matriz.append([])

        print(f'Linha {line} ->', matriz[line])

        for column in range(5):
            # random_number = random.randint(0, 99)
            # while not validate_number(matriz, random_number):
            #     random_number = random.randint(0, 99)
            # matriz[line].append(random_number)

            while True:
                random_number = random.randint(0, 99)

                if validate_number(matriz, random_number):
                    matriz[line].append(random_number)
                    break

    return matriz



def main():
    result = generate_bingo()

    print('Bingo: ', result)

main()
