'''

Desafio 98

Faça um programa que tenha uma função chamada escreva(), que receba
um texto qualquer como parâmetro e mostre uma mensagem com tamanho
adaptável.

Ex. escreva("Olá,Mundo!")

Saída:
----------
Olá,Mundo!
----------
'''


def escreva(txt):
    for l in txt:
        print('~', end='')
    print(f'\n{txt}')
    for l in txt:
        print('~', end='')


escreva("Fagner Ferraz Pavanetti")