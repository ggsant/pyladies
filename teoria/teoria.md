# Teoria

# Listas - Revisão
Quando queremos organizar diversos dados, podemos colocá-los ordenados em uma lista.
Esses dados podem ser de diferentes tipos: inteiros, floats, strings e inclusive outras listas.
* Listas têm itens limitados pelo símbolo de colchetes [ ]
* Listas são mutáveis, ou seja, é possível alterar seus itens: adicionando, removendo e/ou substituindo-os. Poremos usar os métodos: 

append() - adiciona um novo elemento. 

insert() - Adiciona um novo elemento numa determinada posição da 
lista. Todos os elementos daquela posição em diante são deslocados uma posição para frente.

remove() - Remove o primeiro elemento especificado encontrado na lista.

count() - Conta quantas vezes o elemento especificado aparece na lista. Retorna zero se o elemento não pertencer à lista.

clear() - Remove todos os elementos de uma lista. 

extend() - Adiciona todos os elementos da lista passada por parâmetro à lista original. É um tipo de concatenação que não cria uma nova lista.

copy() - Cria uma cópia verdadeira de uma lista. Quando você cria uma variável lista2 = lista1 você está referenciando o mesmo objeto de lista1, portanto todas as alterações que fizer em lista2,
serão aplicadas em lista1. Para evitar esse efeito colateral, utilizamos o copy.

index() - Retorna a posição da primeira ocorrência do elemento especificado. Caso não seja encontrado, um erro será lançado.

pop() - Remove e retorna o elemento da posição especificada. Caso não seja especificada uma posição, removerá o último elemento da lista.

sort() - Caso os elementos tenham implementação do operador menor (<) e sejam comparáveis (normalmente, de mesmo tipo), Python oferece uma função pronta para ordenar seu conteúdo. Caso os elementos não sejam comparáveis, um erro será lançado.

reverse() - Inverte as posições dos elementos de uma lista. O último passa a ser o primeiro, o penúltimo passa a ser o segundo e assim por diante.

list('objeto iterável') - Cria uma lista a partir de um objeto iterável, por exemplo, uma string. Se não for objeto iterável, um
erro será lançado

len(lista) - Retorna o tamanho de uma lista. Funciona para qualquer 
objeto iterável. Se não for um objeto iterável, um erro será lançado.

elemento in lista - Verifica se um elemento está presente em uma lista.

* exemplos: 
lista = ['pyladies', [1,2,3,4], 2020, 9.876]

* Os elementos de uma lista podem ser acessados pelo índice:
cores = ['amarelo','azul', 'verde'];
cores[0]
>> amarelo

* Para percorrer uma lista toda podemos acessar os elementos diretamente ou utilizar os índices para acessá-los:
ex: 
Acessando diretamente:
    for elemento in lista:
        elemento

Acessando através dos indices
    for i in range(len(lista));
        lista[i]

A função range() gera um iterável com N elementos, numerados de 0 a N-1, quando recebe apenas um parâmetro. O formato geral da função range() é:
    range(inicio, fim, passo)
Mas também pode ser escrita como:
    range(inicio, fim)
    range(fim)

* Na função range, início e passo são parâmetros não-obrigatórios, e recebem como valores padrão 0 e 1, respectivamente.
* Fim é um limitante não-inclusivo, isto é, o último elemento será estritamente menor que fim.
* Se for passado apenas um parâmetro, a função considerará como o parâmetro fim, se forem passados dois parâmetros, como início e fim, por padrão.
* Outras duas funções úteis são enumerate e zip.
* Enumerate cria um iterável onde cada elemento é uma tupla com a posição do elemento original da lista e o próprio elemento, respectivamente. exemplo: enumerate(lista)
* Zip cria um iterável onde cada elemento é uma tupla com um elemento da primeira lista na primeira posição, e um elemento da segunda lista na segunda posição. Se uma lista for maior que a outra, zip terá o número de elementos da lista menor. exemplo: zip(lista)


# Lista X Tuplas

Imaginem: Uma empresa organiza de maneira ordenada os horários de saída de um funcionário de todos os dias da semana em uma lista.
Exemplo do funcionário Marcos:

horarios_marcos = ['18:02', '18:05', '19:00', '18:15', '17:04']

João, o secretário desastrado da empresa, resolveu mexer nas listas e acabou substituindo um dos itens por um horário completamente aleatório (‘14:03’).
Marcos foi chamado no RH para explicar porque tinha batido o cartão tão cedo em um dia da semana!
**Como resolver de maneira simples o problema do funcionário Marcos?**

# Tuplas
O Python disponibiliza um tipo muito similar à lista, porém imutável.
As tuplas, geralmente, têm seus itens delimitados pelo símbolo de parênteses () , mas também podem ser declaradas simplesmente por separar os itens com vírgulas, com exceção de quando se quer criar uma tupla vazia.

Os operadores que funcionam com as listas funcionam da mesma forma com as tuplas.
1. Concatenação: tupla + tupla, retorna uma nova tupla.
2. Repetição: tupla * número, retorna uma nova tupla.
3. Indexação e Fatiamento: tupla[número ou intervalo], retorna um item ou vários itens em uma nova tupla.
4. Verificação: item in tupla, retorna booleano.

**ATENÇÃO: tuplas podem conter objetos mutáveis, como listas. Ao inserir um novo número na lista dentro da tupla (posição 0), não alteramos em nada a tupla, já que as referências que ela guarda são as mesmas! Apenas modificamos a lista dentro dela, mas sem mudar o identificador.**

Geralmente, vemos as listas possuindo itens todos do mesmo tipo, enquanto tuplas são mais encontradas obtendo itens de diversos tipos, mas isso não significa que listas não possam ser heterogêneas e tuplas homogêneas!

**As listas são destinadas a serem sequências homogêneas, enquanto que os Tuplas são estruturas de dados heterogêneas.** 

# Dicionários

Dicionário é um objeto que relaciona uma chave a um valor.
A chave é o que indexa um dicionário, isto é, ela corresponde ao conceito de índice, é como se em vez de ter posições 0, 1, 2, 3 e assim por diante, tivéssemos posições com os valores que desejássemos, como “azul”, “amarelo” e “vermelho”. Por se tratarem de índices, uma consequência direta é que as chaves de um dicionários precisam ser únicas, e caso você declare mais de uma vez a mesma chave, o valor será sobreposto.

                        {chave:valor}

* Para criar um dicionário vazio, atribua duas chaves à variável: dicionario = {}

* Para adicionar uma nova chave e valor respectivos à um dicionário existente, ou atualizar um valor de uma chave existente, atribua o novo valor ao dicionário na “posição” da nova chave:
                    dicionario['chave'] = 'valor

* Para verificar se uma chave já existe, utilize o operador in: 'chave' in dicionario 

* Para deletar uma chave e seu valor de um dicionário, utilize o operador del: del(dicionario['chave'])

* Podemos obter todas as chaves de um dicionário com o método keys(): dicionario.keys()

* E também podemos obter todos os valores de um dicionário com o método values(): dicionario.values()

* Para iterar sobre dicionários usando a chave como acesso: 
        for chave in dicionario: 
        dicionario[chave]

* Para iterar sobre os conjuntos chave valor de uma vez:
        for item in dicionario.items(): 
        item 


# Conjuntos

Outra estrutura importante são os conjuntos. Segundo a documentação, um conjunto é: “Um objeto set é uma coleção não ordenada de objetos hasheáveis distintos.” Em python, um conjunto é representado por valores entre chaves.
OBS: cuidado para não confundir com dicionários.

* Declarando um conjunto vazio: conjunto_vazio = set()
* Criando um conjunto a partir de uma lista: novo_conjunto = set(lista)
* Criando um conjunto com valores: novo_conjunto = {1,2,3,4,5}

funções:
* conjunto.add() Adiciona um elemento a um conjunto. Se for duplicado, o conjunto não será alterado.
* conjunto.remove(elemento) Remove um elemento especificado de um conjunto. Se não houver o elemento, um erro será lançado
* len(conjunto) Retorna o tamanho de uma lista. Funciona para qualquer objeto iterável. Se não for um objeto iterável, um erro será lançado.
* elemento in conjunto Verifica se um elemento está presente em um conjunto.
* conjunto.issubset(outro_conjunto) Retorna se um conjunto é subconjunto do outro.
* conjunto.issuperset(outro_conjunto) Retorna se um conjunto é subconjunto do outro
* conjunto.pop() Remove o primeiro elemento do conjunto. Se o conjunto estiver vazio, um erro será lançado.
* conjunto.clear() Remove todos os elementos de um conjunto
* conjunto.union(outro_conjunto) Retorna um novo conjunto com a união dos elementos dos dois conjuntos
* conjunto.isdisjoint(outro_conjunto) Retorna verdadeiro se os conjuntos são disjuntos, isto é, se eles não tem nenhum elemento em comum.
* conjunto.intersection() Retorna um novo conjunto com os elementos comuns entre o primeiro e segundo conjunto. É a operação inversa do symmetric_difference.
* conjunto.intersection_update() Atualiza o primeiro conjunto com os elementos comuns entre o primeiro e segundo conjunto. É a operação inversa do symmetric_difference_update.
* conjunto.difference(outro_conjunto) Retorna um novo conjunto com os elementos do primeiro conjunto não estão contidos no segundo.
* conjunto.difference_update(outro_conjunto) Atualiza os elementos do primeiro conjunto para não conter os elementos contidos no segundo
* conjunto.symmetric_difference() Retorna um novo conjunto com os elementos únicos entre o primeiro e segundo conjunto. É a operação inversa do intersection.
* conjunto.symmetric_difference_update() Atualiza o primeiro conjunto com os elementos únicos entre o primeiro e segundo conjunto. É a operação inversa do intersection_update.

# Funções
Como na maioria das outras linguagens, as funções em python podem conter parâmetros, retorno e tem um escopo, isto é, as variáveis definidas dentro dela não são acessíveis fora naturalmente.
                def nome_da_funcao(parametros):
                codigo
                retorno

# Empacotamento de Argumentos em Python
Os argumentos que passamos normalmente para uma função são conhecidos como argumentos posicionais, por terem que ser passados numa ordem específica e em uma quantidade fixa. Podemos ainda torná-los opcionais ao especificar um valor padrão que será utilizado caso aquele argumento não seja passado.
        def funcao_argumentos_posicionais(arg_um, arg_dois = 0): 
            return arg_um + arg_dois

No entanto, podemos utilizar um número arbitrário de argumentos
utilizado o operador de empacotamento. Ele irá capturar todos os
argumentos passados para função, colocando-os numa tupla.

        def funcao_argumentos_empacotados(*args): 
            sum = 0
            for arg in args:
                sum += arg
            return sum

Podemos ainda utilizá-lo para criar parâmetros nomeados. Estes
poderão ser enviados em qualquer ordem, desde que sejam definidos
pelo seu nome.
        def funcao_argumentos_empacotados(**kwargs):
            if 'nome' in kwargs:
                print(kwargs['nome'])

Caso desejamos utilizar todas as opções possíveis, elas devem ser
declaradas e passadas na função numa ordem específica: argumentos posicionais/opcionais, depois arbitrários, depois nomeados.
        def funcao_tudo_junto(arg_um, arg_opt=none, *args, **kwargs):
            if arg_opt is Nome:
                print('todos os argumentos posicionais:' arg,args)
            else: print("todos os argumentos nomeados:', kwargs)

# Decoradores

Uma função em python é um objeto de primeiro nível. Isso significa que ela funciona como um objeto python, portanto podemos passá-la como parâmetro de uma outra função, e até receber uma função como retorno.
        def printa_nome_func(func):
            print(f'A função passada se chama {func.__name__}.')
        printa_nome_func(len)

Um decorador em Python é nada mais que um açúcar sintático
(syntax sugar) para realizar essa mesma mudança.

O próprio Python já possui inúmeros exemplos de decoradores
muito úteis. O @classmethod e @staticmethod servem para definir
métodos de classe e estáticos, respectivamente.
        class A(object):
        @classmethod
        def foo(cls):
        print(“Método da classe {}”.format(cls.__name__))

# Lambda - função anônima

Funções anônimas são funções extremamente compactas, declaradas numa
única linha sem as palavras reservadas def e return, em seu lugar usamos a palavra reservada lambda.
        lambda parametros: retorno

# Bibliotecas

São conjuntos com subprogramas e funções escritas por outros programadores, que te auxiliam a montar seus códigos.
Vamos estudar:
1. Bibliotecas já existentes e suas funcionalidades.
2. Como criar sua própria biblioteca.

Imagine que você quer fazer um sorteio entre todas as alunas da sala, os nomes estão enumerados então você precisa apenas sortear um número para saber quem é o vencedor. Como faria pra sortear um número sem influenciar no resultado? Existe uma biblioteca para isso, e ela se chama random.

            01 import random
            02 from random import randint
            03 n_alunos = int(input(‘Quantos alunos tem na sala? ‘))
            04 print(‘A aluna na posição’,randint(1,n_alunos), ‘ganhou o sorteio’)

Bibliotecas nativas do Python:
01 - Random: aleatoriedade
02 - Math - Funções Matemáticas
03 - Tkinter - Funções para interfaces
04 - Smtplib - Envio de emails
05 - Time - Controle de tempo
06 - Stdlib (módulo os) - interagir com
o sistema operacional
07 - Muitas outras...

**Para criar sua própria biblioteca é muito fácil, basta apenas você ter dois ou mais programas python salvos na mesma pasta.**

