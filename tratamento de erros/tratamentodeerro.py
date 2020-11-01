
#** exemplo ZeroDivisionError

def divisao(divisor):
    try:
        print(f'Resultado: {42/divisor}')
    except  ZeroDivisionError:
        print('Erro: não pode ser dividido por zero')
print(divisao(2))
print(divisao(12))
print(divisao(0))
print(divisao(1))


