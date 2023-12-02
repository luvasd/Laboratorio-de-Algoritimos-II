class CaixaEletronico:
    def __init__(self):
        self.saldo = 0
        self.transaction_limit = 1000
        self.movimentacoes = []

    def depositar(self, valor):
        try:
            valor = float(valor)
            if valor > 0:
                self.saldo += valor
                self.movimentacoes.append(f'Depósito: +${valor}')
                return f'Depósito de ${valor} realizado com sucesso.'
            else:
                raise ValueError('Valor inválido para depósito. Deve ser maior que zero.')
        except ValueError as e:
            return f'Erro: {e}. Tente novamente.'

    def sacar(self, valor):
        try:
            valor = float(valor)
            if 0 < valor <= self.transaction_limit and valor <= self.saldo:
                self.saldo -= valor
                self.movimentacoes.append(f'Saque: -${valor}')
                return f'Saque de ${valor} realizado com sucesso.'
            else:
                raise ValueError('Valor inválido para saque. Verifique o limite e o saldo disponível.')
        except ValueError as e:
            return f'Erro: {e}. Tente novamente.'

    def verificar_saldo(self):
        return f'Seu saldo atual é de ${self.saldo}'

    def historico_movimentacoes(self):
        return 'Histórico de Movimentações:\n' + '\n'.join(self.movimentacoes)

def main():
    caixa = CaixaEletronico()

    while True:
        print('\nEscolha uma opção:')
        print('1. Depositar dinheiro')
        print('2. Sacar dinheiro')
        print('3. Verificar saldo bancário')
        print('4. Histórico de movimentações')
        print('5. Sair')

        opcao = input('Digite o número da opção desejada: ')

        try:
            opcao = int(opcao)

            if opcao == 5:
                print('Saindo do sistema. Obrigado!')
                break
            elif 1 <= opcao <= 4:
                if opcao == 1 or opcao == 2:
                    valor = input(f'Digite o valor a ser {"depositado" if opcao == 1 else "sacado"}: ')
                    print(caixa.depositar(valor) if opcao == 1 else caixa.sacar(valor))
                else:
                    print(caixa.verificar_saldo() if opcao == 3 else caixa.historico_movimentacoes())
            else:
                raise ValueError('Opção inválida. Escolha uma opção de 1 a 5.')

        except ValueError as e:
            print(f'Erro: {e}. Tente novamente.')

if __name__ == "__main__":
    main()
