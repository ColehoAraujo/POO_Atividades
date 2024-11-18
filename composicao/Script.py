#De volta a parte 2
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0  

#E a parte 3
class Carro(Veiculo):
    def acelerar(self):
        self.velocidade += 10
    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
    def mostrar_velocidade(self):
        print(f"Carro {self.marca} {self.modelo}: {self.velocidade} km/h")

#Finalmente kkk parte 5, Composição...
class Motor:
    """Vai representar um motor com uma potência ESPECÍFICA."""
    def __init__(self, potencia):#Potência do motor (em HP).
        self.potencia = potencia


class CarroComMotor(Carro):
    """CarroComMotor combina a funcionalidade de Carro com a composição de Motor."""
    def __init__(self, marca, modelo, potencia_motor): #Inicializa o Carro com os atributos da classe pai...
        super().__init__(marca, modelo) #Adere um motor ao carro, utilizando a classe Motor.
        self.motor = Motor(potencia_motor)

    def mostrar_potencia_motor(self): #Vai mostrar a potência do motor do carro.
        print(f"Potência do motor: {self.motor.potencia} HP")


#E por fim, testes do carro com motor.
carro_com_motor = CarroComMotor("Chevrolet", "Camaro", 455)
carro_com_motor.acelerar()  #Acelera o carr.
carro_com_motor.mostrar_velocidade()  #Mostra a velocidade depois da aceleração.
carro_com_motor.mostrar_potencia_motor()  #Mostra a potência do motor.