class Super:
    def hello(self):
        print('Olá, sou a super classe')

class Sub (Super):
    def hello(self):
        print('Olá, sou a subclasse')

class SubDaSub(Sub):
    def hello(self):
        print('Olá, sou a subclasse da subclasse')

teste = SubDaSub()
teste.hello()
