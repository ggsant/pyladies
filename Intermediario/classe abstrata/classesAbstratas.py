
#** Uma classe abstrata é uma classe que serve de modelo para outras classes. Ela sempre sera uma superclasse generica, e suas subclasses sao especificas

#** em python utilizamos a biblioteca abc que permite definirmos classes abstratas. Uma classe abstrata deve herdar de ABC(Abstract Base Classes). ABC é a superclasse para classes abstratas.

#** Para definirmos um metodo abstrato, utilizamos o decorador @abstractmethod

#** Vamos supor que desejamos criar uma classe mae chamada FormasGeometricas que tenha os metodos para calcular a area e perimetro e tambem um metodo para imprimir valores


# importar a classe ABC e decorador abstractmethod para o codigo
from abc import ABC, abstractmethod

# Herdar classe ABC para que possamos tornar nossa classe abstrata
class FormasGeometricas(ABC):
    def __init__(self, *lados):
        self.lados = lados
    
    # Decorador que forta o nosso metodo abstrato, ou seja, obrigatoria a implementaçao nas classes filhas
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass # Operação nula utilizada quando o programa requisita sintaticamente que se preencha a lacuna

    def imprime(self):
        print(f'Essa forma tem {self.area()}m² e o perimetro de {self.perimetro()}m')

#** Formas Geometricas

class Quadrado(FormasGeometricas):
    # O * significa que ele recebe n parametros em  forma de tupla
    def __init__(self, *lados):
        super().__init__(*lados)
    
    def area(self):
        return self.lados[0]**2
    
    def perimetro(self):
        return self.lados[0]*4 

    quadrado = Quadrado(5,5,5,5)
    quadrado.imprime()