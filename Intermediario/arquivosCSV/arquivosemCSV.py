
#** O metodo de escrita principal é o csv.writer que tem como parametro obrigatorio o nome do arquivo que sera escrito. Ao utilizar o metido, criamos um objeto do tipo 'csv.writer'. Escrevemos cada linha com o objeto e, como a escrita é feita por linhas, o metodo writerow.

import csv

planilha = open('teste.csv', 'w')

escrever = csv.writer(planilha)
escrever.writerow(['nome', 'Pyladies'])
escrever.writerow(['Gabriela', 'Pyladies São Carlos'])
escrever.writerow(['Rafaela', 'Pyladies Franca'])

planilha.close()

# ** lendo em csv

planilha = open('teste.csv')

ler = csv.reader(planilha)
for row in ler:
    print(row)
    # print(row[0])

planilha.close()

#** Podemos escrever utilizando dicionarios com o metodo DictWriter. Para isso definimos as chaves do dicionario e passar em 'fieldnames' para que o python possa entender as delimitações de cada celula

planilha1 = open('dicionarios.csv', 'w')
titulos = ['Nome', 'Capitulo', 'Banda favorita']

escrita = csv.DictWriter(planilha1, fieldnames=titulos)
escrita.writeheader() #** cabeçalho
escrita.writerow({'Nome': 'Gabriela', 'Capitulo': 'Pyladies São Carlos', 'Banda favorita': 'Racionais'})
escrita.writerow({'Nome':'Leandro', 'Capitulo':'Materiais', 'Banda favorita': 'Barões da pisadinha'})

planilha1.close()

planilha1 = open('dicionarios.csv')
ler = csv.DictReader(planilha1)
for row in ler:
    print(row['Nome'], '-', row['Capitulo'], '-', row['Banda favorita'])
    

