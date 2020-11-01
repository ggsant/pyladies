
#** O python segue uma ordem especifica para percorrer a hierarquia de classes, e essa ordem é chamada de MRO. Com a ordem da esquerda para a direita

#** toda classe tem um atributo _mro_ que podemos acessar atraves do metodo mro() - da classe atual até a classe object. 

"""
Metodos especiais
* os metodos especiais ou magicos em python são utilizados para definir um comportamento especifico para uma classe quando determinada operacao for operada. 

? Inicialização: __init__ 
? Representação: __str__, __repr__, __float__
? Container, sequencia: __len__, __contains__, __iter__, __getitem__
? Numericos: __add__, __mult__, __eq__, __mod__


"""


class Python:
    def saudacao(self):
        print("Ola usuario de python")

class Grupy(Python):
    def saudacao(self):
        print("Ola membro do Grupy")
    pass

class Pylady(Python):
    def saudacao(self):
        print("Ola Pylady")
    pass

class Integrante(Grupy, Pylady):
    pass

gabriela = Integrante()
gabriela.saudacao()
print(Integrante.mro()) #** para verificar a ordem da herança

