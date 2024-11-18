class Veiculo: #Mesmo sistema da parte 2, mas sem o ABC
    def __init__(self, marca, modelo):
        #Atributos comuns a todos os veículos.
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0  #Velocidade inicial do veículo.

#Vamos para a primeira classe de veículo, o carro:
class Carro(Veiculo): #Classe Carro herda os comportamentos gerais de Veiculo generalizando.
    def acelerar(self):
        self.velocidade += 10 #Aumenta a velocidade do carro em 10 km/h.

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10) #Reduz a velocidade do carro em 10 km/h, mas nunca abaixo de 0 poq não tá em ré.

    def mostrar_velocidade(self):
        print(f"Carro {self.marca} {self.modelo}: {self.velocidade} km/h") #Exibe a velocidade atual do carro.

#Agora a outra classe, de moto:
class Moto(Veiculo): #Classe Moto herda os comportamentos gerais de Veiculo geral.
    def acelerar(self):
        self.velocidade += 15 #Aumenta a velocidade da moto em 15 km/h...

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10) #Reduz a velocidade da moto em 10 km/h, mas nunca abaixo de 0, já estabelecemos isso mas estou repetindo.

    def mostrar_velocidade(self): 
        print(f"Moto {self.marca} {self.modelo}: {self.velocidade} km/h") #Exibe a velocidade atual da moto.