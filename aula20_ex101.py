'''

Desafio 101

Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores PARES sorteados pela função anterior.
'''
from random import randint
from time import sleep


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))
        print(lista[c], end=' ')


def somaPar(lista):
    sp = 0
    for i in lista:
        if i % 2 == 0:
            sp = sp + i
    print(f"Somando os valores pares de {lista}, temos {sp}")


valores = list()
sorteia(valores)
print()
sleep(1)
somaPar(valores)