class Animal:
    def __init__(self, nome, peso, idade):
        #* os atributos tem apenas um _ pois ele sao do tipo protected. Ou seja podem ser vistps e modificados pelas classes filhas sem precisar de get e set.
        self._Nome = nome
        self._Peso = peso
        self._Idade = idade
        self._Classe = None
        self._Especies = None
    
    def Infos(self):
        print(f'\nNome: {self._Nome} \nPeso: {self._Peso} \nIdade: {self._Idade} \nClasse: {self._Classe}\nEspecie: {self._Especie}')
    
    def Comer(self):
        print(f'O {self._Especies} está comendo')
    
    def Andar(self):
        print(f'O {self._Especies} está andando')
    