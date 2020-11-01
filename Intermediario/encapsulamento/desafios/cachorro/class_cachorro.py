
class Cachorro:
    def __init__(self, nome, peso, idade, raca):
        #add atributos
        self.__Nome = nome
        self.__Peso = peso
        self.__Idade = idade
        self.__Raca = raca
    #definir os metodos
    def Anda(self):
        print(" O cachorro está andando") 

    def Come(self):
        print("O cachorro está comendo")

    def Dados(self):
        print(f'\nnome:{self.__Nome}\npeso:{self.__Peso}\nidade:{self.__Idade}\nraca:{self.__Raca}')
    
    #getters
    def GetNome(self):
        return self.__Nome
    def GetPeso(self):
        return self.__Peso
    def GetIdade(self):
        return self.__Idade
    def GetRaca(self):
        return self.__Raca
    
    #setters 
    def SetNome(self, valor):
        self.__Nome = valor
    def SetPeso(self, valor):
        self.__Peso = valor
    def SetIdade(self, valor):
        self.__Idade = valor
    def SetRaca(self, valor):
        self.__Raca = valor

cachorro = Cachorro("Scooby", 50, 5, "vira-lata" )

cachorro.SetNome("Rex")
cachorro.SetPeso(35)
cachorro.SetIdade(8)
cachorro.SetRaca('pastor alemão')

cachorro.Dados()

