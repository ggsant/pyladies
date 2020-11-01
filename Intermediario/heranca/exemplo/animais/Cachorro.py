import Animal as an

class Cachorro(an.Animal):
    def __init__(self, Nome, Peso, Idade):
        #* passamos a classe mae como parametro da classe filha. Chamamos o metodo super
        super().__init__(Nome, Peso, Idade)
        self._Classe = "Mamifero"
        self._Especies = "Cachorro"

    def Latir(self):
        print("Au Au Auuuuuuuuu")