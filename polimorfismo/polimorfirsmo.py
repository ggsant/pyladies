
#** Polimorfismo, em python é a capacidade que uma subclasse tem de ter métodos com o mesmo nome de sua superclasse, e o programa saber qual método deve ser invocado, ou seja, o objeto tem a capacitade de assumir diferentes formas

#** Considere a classe Pylady que contem as informações de nome e email de uma integrante

class Pylady:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def imprime(self):
        print(f'Nome: {self.name} - email: {self.email}') 

#** classes filhas
class PyladyUfscar(Pylady):
    def __init__(self, name, email, RA):
        super().__init__(name, email)
        self.RA = RA
    def imprime(self):
        print(f'Nome: {self.name} - email: {self.email} - Ra: {self.RA}') 

class PyladyUsp(Pylady):
    def __init__(self, name, email, nUsp):
        super().__init__(name, email)
        self.nUsp = nUsp
    def imprime(self):
        print(f'Nome: {self.name} - email: {self.email}, nUSP: {self.nUsp}') 

#** lista de pyladies
pyladies = [Pylady('juliana', 'juliana@example.com'), PyladyUfscar('luiza', 'luiza@example.com', 456789), PyladyUsp('Laura', 'la@example.com', 789123)]

for integrante in pyladies:
    integrante.imprime()
