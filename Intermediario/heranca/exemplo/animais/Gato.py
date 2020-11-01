import Animal as an 

class Gato(an.Animal):
    def __init__(self, Nome, Peso, Idade):
        super().__init__(Nome, Peso, Idade)
        self._Classe = "Mamifero"
        self._Especies = "Gato"

    def Miar(self):
        print("Miau miau mimimiau")