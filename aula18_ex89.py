'''

DESAFIO 89

Faça um programa que ajude um jogador da Mega Sena a criar palpites.

O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
lista composta.
'''
from random import sample
from time import sleep
l = []
print('-' * 30)
print(f'{"JOGA NA MEGASENA":^30}')
print('-' * 30)
j = int(input("Quantos jogos você quer que eu sorteie? "))
print(f'-=-= SORTEANDO {j} JOGOS =-=-')
for c in range(j):
    s = sample(range(1, 61), 6)
    l.append(s)
    sleep(0.7)
    print(f"Jogo {c+1}: {s}")
print(f'{"=== BOA SORTE! ===":^30}')
print()
print(f'Lista com os jogos gerados: {l}')