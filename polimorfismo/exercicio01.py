class Programa:
    def __init__(self,nome):
        self.nome = nome
    def imprime(self):
        print(f"Nome do programa: {self.nome}")

class Filme(Programa):
    def __init__(self, nome, duracao):
        super().__init__(nome)
        self.duracao = duracao
    def imprime(self):
        print(f"O filme {self.nome} tem {self.duracao} minutos de duração")

class Serie(Programa):
    def __init__(self, nome, temporadas):
        super().__init__(nome)
        self.temporadas = temporadas
    def imprime(self):
        print(f" A serie {self.nome} tem {self.temporadas} temporadas")

assistirNoFds = [Programa('Fantastico'), Filme('Ta dando onda', 145), Filme('Um contratempo', 159), Serie('Um maluco no pedaço', 8), Serie('Friends',10)]

for programas in assistirNoFds:
    programas.imprime()