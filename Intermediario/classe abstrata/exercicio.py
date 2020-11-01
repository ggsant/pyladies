from abc import ABC, abstractmethod

class Pylady:
    def __init__(self,nome, email):
        self.nome = nome
        self.email = email
    
    @abstractmethod
    def Pasta(self):
        pass
    
    @abstractmethod
    def Funcao(self):
        pass
    
    @abstractmethod
    def Infos(self):
        print(f"A pylady {self.nome} participa da pasta {self.Pasta()}, responsavel por {self.Funcao()}")

class Marketing(Pylady):
    def __init__(self, name, email):
        super().__init__(name, email)
    
    def Pasta(self):
        return 'Marketing'
    
    def Funcao(self):
        return 'responsavel pelo mkt da comunidade'

gabriela = Marketing('gabriela', 'gabriela@gmail.com')
gabriela.Infos()