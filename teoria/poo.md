# Programação Orientada a Objetos

POO é um paradigma da computação. Assim como a Programação Estruturada que é a que utilizamos em todos os nossos programas (Até hoje hehe). 

Programação Estruturada consiste principalmente em:
1. sequências: são os comandos a serem executados
2. condições: sequências que só devem ser executadas se uma condição for satisfeita (exemplos: if-else, switch e comandos parecidos)
3. repetições: sequências que devem ser executadas repetidamente até uma condição for satisfeita (for, while, do-while etc)

Programação estruturada:
Existe uma grande função (ou rotina) que rege o programa.
Claro elas podem ser dividida em sub-rotinas, mas se todas elas fossem adicionadas ao código formaria uma rotina grande

POO consiste principalmente em:
1. Classes: Conjunto de características e comportamentos que definem um objeto.
2. Objetos: é uma instância (ou seja, um exemplar) de uma classe.
3. Os conceitos utilizados na Programação estruturada: sequências, condições, repetições.

Imagine que você quer criar um grupo PyLadies em sua cidade natal.
Para você criar o grupo vai ser necessário seguir certos critérios,
como:
● Ter um nome;
● Quantidade de membros;
● Logo;
● Tem homens? (booleano);
● Nomes dos membros;
● Atividades do grupo;

Desta forma para você criar o grupo, você segue um “molde”, esse molde é a sua CLASSE, e o grupo que você esta criando (assim como outros que já existem) é um OBJETO.

Assim podemos perceber que nossa Classe tem características (atributos) e funções (métodos)

LEMBRETES
1. Não se esqueça dos nomes Atributos e Métodos, pois
eles são os nomes usados em POO.
2. Nome da classe se escreve sempre com letra maiúscula por convenção. 

Classes -> sempre começa com letra maiuscula

Criar a classe: 
* função init inicia quanto o objeto é instanciado! conhecida como metodo construtor. 
class Pyladies:
    def __init__(self, nome_e, quantidade_e, tem_homens_e, nome_dos_membros_e, data_de_criacao_e):
        Para adicionar atributos, utilizamos o self para adicionar os atributos ao proprio objeto
        self.nome = nome_e
        self.quantidade = quantidade_e
        self.tem_homens = tem_homens_e
        self.nome_dos_membros = nome_dos_membros_e
        self.data_de_criacao = data_de_criacao_e
        print('Você criou um objeto! :)

Metodos
    utiliza-se def para criar os metodos. É necessario usar self como paramtro. 

    def Dar_curso(self):
        print("Para dar um curso vc precisa de .....")
    def Apresentar_todas_infos(self):
        print(f"\n{self.nome}\n{self.quantidade}\n{self.tem_homens}\n{self.nome_dos_membros}\n{self.data_de_criacao}")

instanciar o objeto: dentro dos parenteses, nos passamos os atributos como parametros da função
pyladies_brasil= Pyladies("Pyladies Franca", 20, False, "Gabriela, Julia, Carolina, Neide, Creuza", "01/10/2020")

quando fazemos isso, o objeto carrega todas as funções que estão dentro da identação

pyladies_brasil.Dar_curso()
pyladies_brasil.Apresentar_todas_infos()


print('\n', pyladies_brasil.nome)
print('\n', pyladies_brasil.quantidade)
print('\n', pyladies_brasil.tem_homens)
print('\n', pyladies_brasil.nome_dos_membros)
print('\n', pyladies_brasil.data_de_criacao)

# POO - Encapsulamento 
Se alguns desses atributos forem facilmente visíveis e modificáveis, como o Nome do grupo ou a Quantidade de membros, isso pode dar liberdade para que alterações sejam feitas, resultando em efeitos colaterais imprevisíveis.
Nessa analogia, uma pessoa pode confundir alguma variável do programa com um atributo importante, criando efeitos colaterais que podem trazer problemas no futuro para saber a quantidade de membros que havia, por exemplo. Chamamos esse tipo de atributos visíveis.

Na POO, um atributo ou método que não é visível (não é modificável) de fora do próprio objeto é chamado de "privado" e quando é visível, é chamado de "público".

Esse encapsulamento de atributos e métodos impede o chamado vazamento de escopo, onde um atributo ou método é visível por alguém que não deveria vê-lo, como outro objeto ou classe.
Ler ou alterar um atributo encapsulado pode ser feito a partir de getters ( função get() ) e setters ( função set() )

Conclusão
● Para criarmos atributos privados colocamos __NomeDoAtributo.
E para acessa-lo ou modifica-los usamos os métodos get() e set().
Importante
● Além dos atributos privados também existem os atributos
protegidos, para declarar-los usamos _NomeDoAtributo. E os
manipulamos com os mesmos métodos. Explicaremos para que
servem em Heranças.

Métodos getters e setters
● Então como vimos temo os atributos que podem ser públicos,
privados ou protegidos
● Para acessa-los precisamos usar métodos específicos (getters e
setters)
○ No entanto aprendemos a forma tradicional de
implementar esses métodos especiais
○ Existe uma forma pythonica de implementa-los que o que
veremos agora :D

# Herança 

Até agora trabalhamos apenas com as classes Cachorro e Pyladies, certo?
Agora suponha que você também quer ter uma classe Animal. Na hora
de instanciar o teu cachorrinho Rex, você colocaria ele na classe
Cachorro ou Animal?. 

Quando dizemos que uma classe A é um tipo de classe B, dizemos que a classe A herda as características da classe B e que a classe B é mãe da classe A, estabelecendo então uma relação de herança entre elas.

No nosso exemplo o nosso cachorrinho Rex será da classe Cachorro
que é filha da classe Animal

1. Crio a classe Animal normalmente
2. Importo a classe Animal na classe Cachorro
3. Intancio meu objeto normalmente

Mas preste atenção nestes detalhes:
No parâmetro está Animal. Animal pois o nome do arquivo e o nome da classe é o mesmo. Sendo assim a ordem é: NomeArquivo.NomeClasse

Você utiliza super() apenas para o método construtor. Os outros métodos você apenas chama normalmente no Objeto

O método latir() foi o único método implementado na classe Cachorro

self_Classe e self._Especie foram atributos que não pedi no construtor por escolha própria. 

# Polimorfismo