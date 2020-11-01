
# Classes -> sempre começa com letra maiuscula

#Criar a classe: 
#função init inicia quanto o objeto é instanciado! conhecida como metodo construtor. 
class Pyladies:
    def __init__(self, nome_e, quantidade_e, tem_homens_e, nome_dos_membros_e, data_de_criacao_e):
        # Para adicionar atributos, utilizamos o self para adicionar os atributos ao proprio objeto
        self.nome = nome_e
        self.quantidade = quantidade_e
        self.tem_homens = tem_homens_e
        self.nome_dos_membros = nome_dos_membros_e
        self.data_de_criacao = data_de_criacao_e
        #print('Você criou um objeto! :) ') #função
    #Metodos
    #utiliza-se def para criar os metodos. É necessario usar self como paramtro. 
    def Dar_curso(self):
        print("Para dar um curso vc precisa de .....")
    def Apresentar_todas_infos(self):
        print(f"\n{self.nome}\n{self.quantidade}\n{self.tem_homens}\n{self.nome_dos_membros}\n{self.data_de_criacao}")

# instanciar o objeto:
#dentro dos parenteses, nos passamos os atributos como parametros da função
pyladies_brasil= Pyladies("Pyladies Franca", 20, False, "Gabriela, Julia, Carolina, Neide, Creuza", "01/10/2020")

# quando fazemos isso, o objeto carrega todas as funções que estão dentro da identação

pyladies_brasil.Dar_curso()
pyladies_brasil.Apresentar_todas_infos()


# print('\n', pyladies_brasil.nome)
# print('\n', pyladies_brasil.quantidade)
# print('\n', pyladies_brasil.tem_homens)
# print('\n', pyladies_brasil.nome_dos_membros)
# print('\n', pyladies_brasil.data_de_criacao)