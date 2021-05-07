'''

DESAFIO 75 - MAIOR E MENORES VALORES EM TUPLA

Crie um programa que vai gerar cinco números aleatórios e colocar em
uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.
'''

from random import randint

'''tupla = tuple(randint(i + 0, 10) for i in range(0, 5))
# 1o gera tupla 2o chama função 3o escopo i + de tanto a tanto 4o para i de 0 a 5 (número de vezes que o for será realizado)'''

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print("Os números sorteados foram ", end=' ')
for numeros in tupla:
    print(numeros, end= ' ')
print(f"\nMaior valor: {max(tupla)}; menor valor: {min(tupla)}")




