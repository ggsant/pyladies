class Pyladies:
    def __init__(self, nome_e, quantidade_e, tem_homens_e, nome_dos_membros_e, data_de_criacao_e):
        self.__Nome = nome_e
        self.__Quantidade = quantidade_e
        self.__Tem_homens = tem_homens_e
        self.__Nome_dos_membros = nome_dos_membros_e
        self.__Data_de_criacao = data_de_criacao_e
        self.__Creators = {"nome":[], "email":[]} #dicionario
        
    def Dar_curso(self):
        print("Para dar um curso vc precisa de .....")
    def Apresentar_todas_infos(self):
        print(f"\n {self.nome}\n{self.quantidade}\n{self.__Tem_homens}\n{self.__Nome_dos_membros}\n{self.data_de_criacao}")
        
    #getters
    def GetNome(self):
        return self.__Nome
    def GetQuantidade(self):
        return self.__Quantidade
    def GetTemHomens(self):
        return self.__Tem_homens
    def GetNomeGrupo(self):
        return self.__Nome_dos_membros
    def GetData(self):
        return self.__Data_de_criacao
    def GetCreators(self):
        if self.__Creators["nome"] == []:
            return None
        else:
            return self.__Creators
    
    #setters
    def SetNome(self, valor):
        self.__Nome = valor
    def SetQuantidade(self, valor):
        self.__Quantidade = valor
    def SetTemHomens(self, valor):
        self.__Tem_homens = valor 
    def SetNomeGrupo(self, valor):
        self.__Nome_dos_membros = valor
    def SetData(self, valor):
        self.__Data_de_criacao = valor
    def SetCreators(self, nome, email):
        self.__Creators["nome"].append(nome)
        self.__Creators["email"].append(email)
    
