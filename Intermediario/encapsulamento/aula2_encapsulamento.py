# Encapsulamento

# O que os comandos dps do objeto ser instanciado vão fazer ? 

class Pyladies:
    def __init__(self, nome_e, quantidade_e, tem_homens_e, nome_dos_membros_e, data_de_criacao_e):
        self.nome = nome_e
        self.quantidade = quantidade_e
        self.__Tem_homens = tem_homens_e
        self.__Nome_dos_membros = nome_dos_membros_e
        self.data_de_criacao = data_de_criacao_e
        
    def Dar_curso(self):
        print("Para dar um curso vc precisa de .....")
    def Apresentar_todas_infos(self):
        print(f"\n{self.nome}\n{self.quantidade}\n{self.__Tem_homens}\n{self.__Nome_dos_membros}\n{self.data_de_criacao}")
    #getters
    def GetNomeGrupo(self):
        return self.__Nome_dos_membros
    #setters
    def SetNomeGrupo(self, valor):
        self.__Nome_dos_membros = valor


pyladies_brasil= Pyladies("Pyladies Franca", 20, False, "Gabriela, Julia, Carolina, Neide, Creuza", "01/10/2020")

# mudar os atributos 
# Se alguns desses atributos forem cfacilmente visiveis e modificaveis, como o Nome ou quantidade, isso pode dar liberdade para que as alterações sejam feitas, resultanto em efeitos colaterais imprevisiveis
# um atributo ou metodo que nao é visivel/modificavel de fora do proprio objeto é chamado de privado, e quando é visivel é chamado de publico 
# para deixar privado, basta botar dois _ na frente do atributo, por ex: __quantidade
# Esse encapsulamento de atributos e metodos impede o vazamento de escopo, onde um atributo ou um metodo é visivel por alguem que nao deveria ve-lo, como outro objeto ou classe 
# Ler ou alterar um atributo encapsulado pode ser feito a partir de getters (função get() ) ou setters (função set())
pyladies_brasil.quantidade = 1000
pyladies_brasil.nome = "São Carlos"
pyladies_brasil.__Tem_homens = True # privado
pyladies_brasil.__Nome_dos_mebros = " auisiahsiahsiahishazihsiahsiau" # nao muda pq é privado
# para mudar usamos o set
pyladies_brasil.SetNomeGrupo("Priscila, Monica, Lara ")


print(pyladies_brasil.GetNomeGrupo())

pyladies_brasil.Dar_curso()
pyladies_brasil.Apresentar_todas_infos()

# temos tbm atributos protegidos, que tem somente um underline na frente