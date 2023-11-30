def TipoTriangulo(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Os lados fornecidos não formam um triângulo válido.")

    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def main():
    try:
        lado1 = float(input("Digite o comprimento do primeiro lado: "))
        lado2 = float(input("Digite o comprimento do segundo lado: "))
        lado3 = float(input("Digite o comprimento do terceiro lado: "))

        tipo = TipoTriangulo(lado1, lado2, lado3)
        print(f"O triângulo é {tipo}.")
    except ValueError as e:
        print("Erro", e) 

main()
