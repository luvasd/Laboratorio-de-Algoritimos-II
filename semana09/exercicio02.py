def avaliar_produto():
    try:
        nota = int(input("Digite uma nota para o produto (de 0 a 10): "))

        assert 0 <= nota <= 10, "A nota deve estar no intervalo de 0 a 10."

        print(f"A nota {nota} foi registrada com sucesso.")
    
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
    except AssertionError as e:
        print(f"Erro: {e}")

avaliar_produto()
