
class Pyladies:
    def __init__(self, nome, quantidade, tem_homens):
        self.__setado = False
        self.nome = nome
        self.quantidade = quantidade
        self.Tem_homens = tem_homens
        self.__setado = True

#* Property é um decorador. Um decorador pega uma função e da uma nova funcionalidade para ela. É uma função que tem outra função como parametro. 
#* o Property cria um get para os atributos
    @property #*Metodo get
    def Nome(self):
        return f"O nome do capitulo é {self.__Nome}"

    @Nome.setter #* modifica o valor
    def Nome(self, nome):
        if self.__setado == False:
            self.__Nome = nome
        else:
            x = input("Certeza que quer mudar o nome? (s/n)")
            if x == 's':
                self.__Nome = nome

pyladies_sanca = Pyladies('Pyladies São Carlos', 18, True)

pyladies_sanca.Nome = " Pyladies Saõ carlos USP"
print(pyladies_sanca.Nome)
