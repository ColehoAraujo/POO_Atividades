from abc import ABC, abstractmethod

class Veiculo(ABC): #A classe é abstrata, ent serve como base para outros veículos.
    def __init__(self, marca, modelo): #Atributos comuns a todos os veículos.
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0 #Vamo por velocidade start 0, ate porq ngm começa ja a 100km/h

        @abstractmethod #Método Abstrato, Cami prefere sem method, mas ajuda de vez em quando.
        def acelerar(self): #Basicamente o método vai obrigar as classes filhas a implementar.
            pass #O pass serve como um passe mesmo, é um espaço reservado de uma instrução , mas nenhum código real é necessário

        
        @abstractmethod #Mesma coisa
        def frear(self):
            pass

        @abstractmethod #E mesma coisa
        def mostrar_velocidade(self):
            pass

#Explicação Detalhada: A abstração remove detalhes desnecessários.
#Isso permite que o código foque nos métodos "Acelerar", "Frear" e "Mostrar_Velocidade", que definem todos os veículos.