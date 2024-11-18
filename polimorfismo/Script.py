#Novamente, vamos repescar a Parte 2, sem o ABC
class Veiculo:
    def __init__(self, marca, modelo):
        # Atributos que são comuns a todos os veículos.
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0  # Velocidade inicial do veículo é sempre 0.

#E agora a parte 3, herança
class Carro(Veiculo):
    def acelerar(self):
        self.velocidade += 10
    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
    def mostrar_velocidade(self):
        print(f"Carro {self.marca} {self.modelo}: {self.velocidade} km/h")

class Moto(Veiculo):
    def acelerar(self):
        self.velocidade += 15
    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
    def mostrar_velocidade(self):
        print(f"Moto {self.marca} {self.modelo}: {self.velocidade} km/h")

#Para que finalmente nosso polimorfismo funcione corretamente
def teste_veiculo(veiculo):
    """Função genéricássa, basicamente testa veículos, e mostra como polimorfismo permite que objetos de diferentes classes sejam tratados de forma uniforme."""
    veiculo.acelerar()  #Chama o método acelerar pela 1meira vez.
    veiculo.acelerar()  #Chama o método acelerar pela 2nda vez.
    veiculo.mostrar_velocidade()  #Mostra a velocidade atual após as acelerações.
    veiculo.frear()  #Chama o método frear.
    veiculo.mostrar_velocidade()  #E por fim, a velocidade após a frenagem.


#Teste1, com um carro.
carro = Carro("Ford", "Fiesta")
teste_veiculo(carro)  #Testa o carro com as operações de acelerar e frear...

#Teste2, com uma moto.
moto = Moto("Honda", "CB500")
teste_veiculo(moto)  #Testa a moto, também com as operações de acelerar e frear.