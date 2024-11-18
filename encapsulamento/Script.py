class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo = 0):
        self._numero_conta = numero_conta #Atributo Privadis
        self._titular = titular #Atributo Privadis
        self._saldo = saldo #Atributo Privadis
    
    def depositar (self, valor):
        """Adiciona um valor ao saldo."""
        if valor > 0:
            self._saldo += valor
        else:
            raise ValueError("O valor do depósito deve ser positivo... Já viu depositar negativo?")
    
    def sacar(self,valor):
        """Remove um valor do saldo, SE possível."""
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else:  
            raise ValueError("Saldo insuficiente... Pobre.")
        
    def consultar_saldo(self):
        """Retorna o saldo atual."""
        return self._saldo
    
#Testes abaixo
conta = ContaBancaria("12345-6", "Bel", 1000)
conta.depositar(200)
print(conta.consultar_saldo()) #Se der certo vai ser 1200 (1000 + 200)
conta.sacar(500)
print(conta.consultar_saldo()) #Se der certo vai ser 700 (1200 - 500)

#Explicação detalhada: O Encapsulamento protege os atributos "_numero_conta", "_titular" e "_saldo";
#Isso garante com que eles sejam só acessados ou modificados via métodos específicos, como "depositar", "sacar" ou "consultar_saldo".