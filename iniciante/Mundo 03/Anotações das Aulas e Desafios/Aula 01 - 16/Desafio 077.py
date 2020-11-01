"""
DESAFIO 077: Contando Vogais em Tupla

Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
vogais = 'aeiou'

for p in palavras:
    v = ''
    for letra in p:
        if letra in vogais:
            v += ' ' + letra

    print(f'Na palavra {p.upper()} temos as vogais:{v}')
