'''

Desafio 99

Faça um programa que tenha uma função chamada contador(), que receba
três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.
'''
from time import sleep


def contador(i, f, p):
    print('-' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if f > i:
        f = f + 1
    else:
        f = f - 1
    if i > f and p > 0:
        p = -p
    if i < f and p < 0:
        p = p * -1
    if p == 0:
        if i > f:
            p = p -1
        else:
            p = p +1
    for c in range(i, f, p):
        print(f'{c}', end=' ')
        sleep(0.5)
    print(" FIM!")
    print('-' * 30)


contador(1, 10, 1)
print()
contador(10, 0, -2)
print()
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Qual o ínicio? "))
fim = int(input("Qual o fim? "))
passo = int(input("Qual o passo? "))
contador(inicio, fim, passo)

