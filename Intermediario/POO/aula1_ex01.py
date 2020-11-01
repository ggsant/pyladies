# criar uma classe dos exemplos de cachorro

class Cachorro:
    def __init__(self, nome_e, peso_e, altura_e, raca_e):
        #add atributos
        self.nome = nome_e
        self.peso = peso_e
        self.altura = altura_e
        self.raca = raca_e
    #definir os metodos
    def Anda(self):
        print(" O cachorro está andando") 

    def Come(self):
        print("O cachorro está comendo")
    
    def Infos(self):
        print(f" Nome: {self.nome}\n Peso: {self.peso}\n Altura: {self.altura}cm\n Raca: {self.raca}")


cachorro = Cachorro("Scooby", 50, 30, "vira-lata" )

cachorro.Anda()
cachorro.Come()
cachorro.Infos()
