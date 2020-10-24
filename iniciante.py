# Variaveis: Para declararmos uma varíavel em python é um processo muito simples e fácil, basta dar um nome para a varíavel e definir um valor com algum dos tipos primitivos? String, inteiro, float, bool

# Exemplos
nome = "gabriela";
idade = 32;
altura = 1.75;
ligado = False;

#variaveis na pratica: 
#calcular a soma de dois numeros
numero1 = 10
numero2 = 5
calcular = numero1 + numero2
resultado = calcular

print(resultado) # saída =  15

# Da o nome completo
nome = "João"
sobrenome = "de Oliveira"
nomeCompleto = nome + " " + sobrenome
resultado = nomeCompleto

print(nomeCompleto) # saída =  João de Oliveira

#Para capturarmos uma entrda do usuário iremos utilizar a função input()
entradaUsuario = input('Informe o seu primeiro nome! ')
resultado = entradaUsuario
print(resultado) # saida = "o nome digitado pelo usuário"

#Funções no python são importantes para executarmos algumas tarefas e operações matemática

#Para criarmos uma definição iremos fazer uso de uma palavra reservada do Python chamada def e o nome da sua função, veja logo abaixo como criar suas primeira função.

#Uma função no python pode receber um parâmetro ou varios, e pode também não receber nenhum parâmetro como no exemplo acima, nos exemplos abaixo iremos mostrar a declaração de algumas funções recebendo 1 e 2 parâmetros.

def digaSeuNome():
  print("Meu nome é Ronaldo!")


def informeSeuNome(nome):
  print("O seu nome é " + nome)

informeSeuNome("Thalita Silva")

def informeSeuNomeEDataNacimento(nome, dataNascimento):
  print("O seu nome é " + nome + " e sua da de Nascimento é " + dataNascimento)
   # saida = "O seu nome é Thalita Silva e sua da de Nascimento é 14/04/1500"

informeSeuNomeEDataNacimento("Thalita Silva", "14/04/1500")

#O Python assim como em outras liguagem de programação temos os operadores aritmeticos que são utilizado para a execução de operações matemáticas
# adição
print(5 + 2)  # saida 7

# subtração
print(5 - 2)  # saida 3

# multiplicação
print(5 * 2)  # saida 10

# divisão
print(15 / 3 ) # saida 5

# exponenciação
print(2 ** 2)  # saida 32

# parte inteira
print(10 // 9)   # saida 1

# módulo ou mod
print(4 % 2)  # saida 0

#logicos

# Maior que
print(5 > 2)  # saida True

# Menor que
print(5 < 2)  # saida True

# Maior ou igual
print(5 >= 6)  # saida False

# Menor ou igual
print(15 <= 3 ) # saida False

# Igual a 
print(2 == 2)  # saida True

# Diferente de 
print(2 != 2)  # saida false

#Nas estruturas condicionais em Python temos os if, elif, else que são muito úteis na tomada de decição de uma tarefa.

#Nas condicionais simples temos apenas uma possibilidade de comparação para uma tomada de decisão.
# Exemplo 1:
# Digamos que estão somando dois valores e queremos ter certeza que o resultado seja maior que 0, podemos checar essa possibilidade com uma condicional bem simples como no código em python abaixo:


soma = 10 + 5

if soma > 0:
  print("O resultado da soma é maior que zero")
else:
  print("O resultado da soma não é maior que zero")

#Exemplo 2: Digamos que estão verificando se o nome de uma pessoa está correto, podemos checar também com uma condicional bem simples como no código em python abaixo:
nome = "Alexandre"

if nome == "Alexandre":
  print("O nome está correto!")
else:
  print("O nome está errado!")

# Nas condicionais composta temos comparar varias possibilidade para uma determinada decisão, mas não se assuste pois assim como as anteriores a implementação delas são bastantes simples.
# Exemplo 1: Imagine um cenário onde queremos identificar se o nome de uma pessoa está correto e se ela é maior de idade, para fazermos essa checagem usaremos um operador que ainda não foi visto por nós nesse guia para iniciantes que é o and
nome = "Alexandre"
idade = 17

if nome == "Alexandre" and idade >= 18:
  print("O seu está correto e você é maior de idade")
else:
  print("O nome está errado ou você não é maior de idade!")

# Os laços de repetição no Python assim como em outras linguagem são utilizado para percorrer um Array, tuples ou Dictionary, ou simplesmente fazer algum tipo de contagem.

#for
#Exemplo 1: Imagine um cenário onde temos que contar de 0 até 100 podemos utilizar o for para nos auxiliar nessa contagem.  No exemplo abaixo utilizamos uma varíavel com o nome de i que será incrementada e mostrada na tela do usuário até que seu valor seja igual a 100, Mas você deve está se perguntando por que colocamos no range(101), se tivessemos colocado dentro do range(100), o contado iria mostra todos os valores de 0 até 99, mas no exemplo atual queremos que os valores fossem mostrados de 0 até 100
for i in range(101):
  print(i)

for i in range(30, 41):
  print(i)

# Enquanto o laço de repetição for, faz a contagem de acordo com o que está definido no seu range o while é um pouquinho diferente mas nada muito complicado, utilizaremos os mesmo exemplos do for para que você possa entender que os dois podem resolver os mesmo tipos de problemas, mas com abordagens diferentes.
#Exemplo 1: Imagine um cenário onde temos que contar de 0 até 100 podemos utilizar o for para nos auxiliar nessa contagem.
contador = 0
while contador < 100:
  print(contador)
contador = contador + 1