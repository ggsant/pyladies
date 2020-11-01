#* fazer 
class InfoMembros:
    def __init__(self):
        self.__InfoMembros = {'nome': {'nascimento': [], 'universidade': [], 'curso': []}}
    
    def GetInfoMembros(self): 
        return self.__Info_membros

    def SetInfoMembros(self, nome, nascimento, universidade, curso):
        self.__Info_membros ['nome'].append(nome)
        self.__Info_membros ['nascimento'].append(nascimento)
        self.__Info_membros ['universidade'].append(universidade)
        self.__Info_membros ['curso'].append(curso)
    
    def MostraInfo(self):
        print(self.__Info_membros)

infoMembros = InfoMembros('gabriela': {'nascimento': 19.01, 'universidade': 'usp', 'eng eletrica'})


infoMembros.MostraInfo()