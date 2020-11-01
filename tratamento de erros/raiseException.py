
#** Agora saiba que é possivel erguer erros para o seu proprio codigo. Erguer uma exceção é um jeito de dizer 'Pare de executar o código dessa função e vá para o bloco except'
#** raise keyword / chamada para a funçao Exception()
#** Uma String contendo uma mensagem de erro util passada para a função exception 

def boxPrint(simbolo, largura, altura):
    if len(simbolo) != 1:
        raise Exception('Simbolo tem apenas um caractere')
    if largura <= 2:
        raise Exception('Largura deve ser maior do que 2')
    if altura <= 2:
        raise Exception('Altura deve ser maior do que 2')

    print(simbolo*largura)
    for i in range(altura-2):
        print(simbolo + (' ' * (largura - 2)) + simbolo)
    print(simbolo*largura)

for sym, w, h in (('@',4,4), ('0',20,5), ('x',1,3), ('ZZ',3,3)):
    try: 
        boxPrint(sym, w, h)
    except  Exception as error:
        print('An exception happened:' + str(error))