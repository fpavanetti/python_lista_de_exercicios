'''

DESAFIO 47 - CONTAGEM REGRESSIVA

Faça um programa que mostre na tela uma
contagem regressiva para o estouro de
fogos de artíficio, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.


'''
from time import sleep
import emoji
print("Contagem regressiva para o ano novo!")
for c in range (10, 0-1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(":fireworks: \033[1;33m FELIZ ANO NOVO!!! \033[m :fireworks:"))