

#principal
# é pra importar o nome do arquivo
# geralmente utilizamos o mesmo nome da classe no arquivo
# o asterisco diz que é para importar tudo do documento
from Pyladies import *

pyladies_brasil= Pyladies("Pyladies Franca", 20, False, "Gabriela, Julia, Carolina, Neide, Creuza", "01/10/2020")

pyladies_brasil.SetNomeGrupo("Priscila, Monica, Lara ")
pyladies_brasil.SetCreators("gabriela" ,"gabriela@teste.com")
pyladies_brasil.SetCreators("monica" ,"monica@teste.com")
print(pyladies_brasil.GetCreators())
print(pyladies_brasil.GetNomeGrupo())
