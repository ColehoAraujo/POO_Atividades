class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0): #criação dos atributos privados (AP)
        self._numero_conta = numero_conta #AP
        self._titular = titular #AP
        self._saldo = saldo #AP

    def depositar(self, valor):
        """Adiciona um valor ao saldo."""
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Erro: O valor do depósito deve ser positivo, não dá pra adicionar algo negativo.")

    def sacar(self, valor):
        """Remove um valor do saldo, se possível."""
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Erro: Saldo insuficiente... pobre.")

    def consultar_saldo(self):
        """Retorna o saldo atual."""
        print(f"Saldo atual: R${self._saldo:.2f}")


def menu():
    print("\n=== Bem-vindo ao Banco Bel ===")
    print("\nDigite seus dados, caso não tenha um registro, vamos criar ele agora.")
    numero_conta = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    conta = ContaBancaria(numero_conta, titular)

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Consultar saldo")
        print("4. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor a depositar: R$"))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a sacar: R$"))
            conta.sacar(valor)
        elif opcao == "3":
            conta.consultar_saldo()
        elif opcao == "4":
            print("Obrigado por usar o Banco Bel. Até!")
            break
        else:
            print("Opção inválida, é de 1 a 4. Tente novamente.")


# Início do programa
if __name__ == "__main__":
    menu()